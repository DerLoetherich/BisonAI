import time
import copy

INFINITY = float('inf')
NEG_INFINITY = float('-inf')

#define Game state
def starting_board():
    return [
    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    [None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, 'D', 'D', 'I', 'D', 'D', None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None],
    ]


def possible_moves_dog(board):
    possible_moves = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'D':
                # Check horizontal moves to the right
                for c in range(j+1, len(board[0])):
                    if board[i][c] is None:
                        possible_moves.append(((i, j), (i, c)))
                    else:
                        break
                # Check horizontal moves to the left
                for c in range(j-1, -1, -1):
                    if board[i][c] is None:
                        possible_moves.append(((i, j), (i, c)))
                    else:
                        break
                # Check vertical moves up
                for r in range(i-1, 0, -1):
                    if board[r][j] is None:
                        possible_moves.append(((i, j), (r, j)))
                    else:
                        break
                # Check vertical moves down
                for r in range(i+1, len(board)-1):
                    if board[r][j] is None:
                        possible_moves.append(((i, j), (r, j)))
                    else:
                        break
                # Check diagonal moves up-right
                for r, c in zip(range(i-1, 0, -1), range(j+1, len(board[0]))):
                    if board[r][c] is None:
                        possible_moves.append(((i, j), (r, c)))
                    else:
                        break
                # Check diagonal moves up-left
                for r, c in zip(range(i-1, 0, -1), range(j-1, -1, -1)):
                    if board[r][c] is None:
                        possible_moves.append(((i, j), (r, c)))
                    else:
                        break
                # Check diagonal moves down-right
                for r, c in zip(range(i+1, len(board)-1), range(j+1, len(board[0]))):
                    if board[r][c] is None:
                        possible_moves.append(((i, j), (r, c)))
                    else:
                        break
                # Check diagonal moves down-left
                for r, c in zip(range(i+1, len(board)-1), range(j-1, -1, -1)):
                    if board[r][c] is None:
                        possible_moves.append(((i, j), (r, c)))
                    else:
                        break

    return possible_moves


def possible_moves_bison(board):
    possible_moves = []
    for i in range(len(board)-1):
        for j in range(len(board[0])):
            if board[i][j] == 'B' and board[i+1][j] == None:
                possible_moves.append(((i, j), (i+1, j)))
    return possible_moves


def possible_moves_indian(board):
    possible_moves = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'I':
                # Check vertical moves
                if i-1 >= 0 and board[i-1][j] in [None, 'B']:
                    possible_moves.append(((i, j), (i-1, j)))
                if i+1 < len(board) and board[i+1][j] in [None, 'B']:
                    possible_moves.append(((i, j), (i+1, j)))
                # Check horizontal moves
                if j-1 >= 0 and board[i][j-1] in [None, 'B']:
                    possible_moves.append(((i, j), (i, j-1)))
                if j+1 < len(board[0]) and board[i][j+1] in [None, 'B']:
                    possible_moves.append(((i, j), (i, j+1)))
                # Check diagonal moves
                if i-1 >= 0 and j-1 >= 0 and board[i-1][j-1] in [None, 'B']:
                    possible_moves.append(((i, j), (i-1, j-1)))
                if i-1 >= 0 and j+1 < len(board[0]) and board[i-1][j+1] in [None, 'B']:
                    possible_moves.append(((i, j), (i-1, j+1)))
                if i+1 < len(board) and j-1 >= 0 and board[i+1][j-1] in [None, 'B']:
                    possible_moves.append(((i, j), (i+1, j-1)))
                if i+1 < len(board) and j+1 < len(board[0]) and board[i+1][j+1] in [None, 'B']:
                    possible_moves.append(((i, j), (i+1, j+1)))
    return possible_moves


def possible_moves_dog_and_indian(board):
    pm = possible_moves_dog(board)
    pm = pm + possible_moves_indian(board)
    return pm

def move_piece(move, board):
    # Move the piece
    piece_type = board[move[0][0]][move[0][1]]
    board[move[0][0]][move[0][1]] = None
    board[move[1][0]][move[1][1]] = piece_type
    return board

def possible_moves(board, player):
    if player == True:
        return possible_moves_bison(board)
    elif player == False:
        return possible_moves_dog_and_indian(board)
    else:
        raise ValueError('Invalid player')

def game_over(board):
    bison_moves = possible_moves_bison(board)
    val = (False, None)
    for f in board[6]:
        if f == 'B':
            return (True, True)
    if not bison_moves:
        val = (True, False)
    return val

def other_player(player):
    if player == True:
        return False
    elif player == False:
        return True
    else:
        raise ValueError('Invalid player')
        

def print_board(board):
    print("   0 1 2 3 4 5 6 7 8 9 10 11")
    print("   -----------------------")
    for row in range(7):
        print(row, end=" |")
        for col in range(11):
            if board[row][col] is None:
                print("  ", end="")
            else:
                print(f" {board[row][col]}", end="")
        print(" |")
    print("   -----------------------")