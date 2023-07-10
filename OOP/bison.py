import numpy as np

def board():
    return np.array([
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0,  0, 2, 2, 3, 2, 2, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

def possible_moves_dog(board):
    possible_moves = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 2:
                # Check horizontal moves to the right
                for c in range(j+1, len(board[0])):
                    if board[i][c] == 0:
                        possible_moves.append(((i, j), (i, c)))
                    else:
                        break
                # Check horizontal moves to the left
                for c in range(j-1, -1, -1):
                    if board[i][c] == 0:
                        possible_moves.append(((i, j), (i, c)))
                    else:
                        break
                # Check vertical moves up
                for r in range(i-1, 0, -1):
                    if board[r][j] == 0:
                        possible_moves.append(((i, j), (r, j)))
                    else:
                        break
                # Check vertical moves down
                for r in range(i+1, len(board)-1):
                    if board[r][j] == 0:
                        possible_moves.append(((i, j), (r, j)))
                    else:
                        break
                # Check diagonal moves up-right
                for r, c in zip(range(i-1, 0, -1), range(j+1, len(board[0]))):
                    if board[r][c] == 0:
                        possible_moves.append(((i, j), (r, c)))
                    else:
                        break
                # Check diagonal moves up-left
                for r, c in zip(range(i-1, 0, -1), range(j-1, -1, -1)):
                    if board[r][c] == 0:
                        possible_moves.append(((i, j), (r, c)))
                    else:
                        break
                # Check diagonal moves down-right
                for r, c in zip(range(i+1, len(board)-1), range(j+1, len(board[0]))):
                    if board[r][c] == 0:
                        possible_moves.append(((i, j), (r, c)))
                    else:
                        break
                # Check diagonal moves down-left
                for r, c in zip(range(i+1, len(board)-1), range(j-1, -1, -1)):
                    if board[r][c] == 0:
                        possible_moves.append(((i, j), (r, c)))
                    else:
                        break

    return possible_moves


def possible_moves_bison(board):
    possible_moves = []
    for i in range(len(board)-1):
        for j in range(len(board[0])):
            if board[i][j] == 1 and board[i+1][j] == 0:
                possible_moves.append(((i, j), (i+1, j)))
    return possible_moves


def possible_moves_indian(board):
    possible_moves = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 3:
                # Check vertical moves
                if i-1 >= 0 and board[i-1][j] in [0, 1]:
                    possible_moves.append(((i, j), (i-1, j)))
                if i+1 < len(board)-1 and board[i+1][j] in [0, 1]:
                    possible_moves.append(((i, j), (i+1, j)))
                # Check horizontal moves
                if j-1 >= 0 and board[i][j-1] in [0, 1]:
                    possible_moves.append(((i, j), (i, j-1)))
                if j+1 < len(board[0]) and board[i][j+1] in [0, 1]:
                    possible_moves.append(((i, j), (i, j+1)))
                # Check diagonal moves
                if i-1 >= 0 and j-1 >= 0 and board[i-1][j-1] in [0, 1]:
                    possible_moves.append(((i, j), (i-1, j-1)))
                if i-1 >= 0 and j+1 < len(board[0]) and board[i-1][j+1] in [0, 1]:
                    possible_moves.append(((i, j), (i-1, j+1)))
                if i+1 < len(board)-1 and j-1 >= 0 and board[i+1][j-1] in [0, 1]:
                    possible_moves.append(((i, j), (i+1, j-1)))
                if i+1 < len(board)-1 and j+1 < len(board[0]) and board[i+1][j+1] in [0, 1]:
                    possible_moves.append(((i, j), (i+1, j+1)))
    return possible_moves


def possible_moves_dog_and_indian(board):
    pm = possible_moves_dog(board)
    pm = pm + possible_moves_indian(board)
    return pm

def possible_moves(board, current_player):
    if current_player == True:
        return possible_moves_bison(board)
    elif current_player == False:
        return possible_moves_dog_and_indian(board)
    else:
        raise ValueError('Invalid player')

def make_move(board, move):
    # Move the piece
    piece_type = board[move[0][0]][move[0][1]]
    board[move[0][0]][move[0][1]] = 0
    board[move[1][0]][move[1][1]] = piece_type
    return board

def is_game_over(board):
    bison_moves = possible_moves_bison(board)
    val = False
    for f in board[6]:
        if f == 1:
            return True
    if not bison_moves:
        val = True
    return val

def get_result(board):
    if is_game_over(board):
        bison_moves = possible_moves_bison(board)
        for f in board[6]:
            if f == 1:
                return +1
            elif not bison_moves:
                return -1


def display_board(board):
    print("   -----------------------")
    for row in range(len(board)):
        print(row, end=" |")
        for col in range(len(board[0])):
            if board[row][col] == 0:
                print("  ", end="")
            else:
                print(f" {board[row][col]}", end="")
        print(" |")
    print("   -----------------------")


def winning_board():
    return np.array([[1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 2, 3, 2, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])

def test_board():
    return np.array([[1, 1, 1],
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 3, 0],
                    [0, 0, 0]])