class Game:
    def __init__(self,
                  board = [
                    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
                    [None, None, None, None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None, None, None, None],
                    [None, None,  None, 'D', 'D', 'I', 'D', 'D', None, None, None],
                    [None, None, None, None, None, None, None, None, None, None, None]],
                  currentPlayer = True,
                  last_move = None):
        self.board = board
        self.currentPlayer = currentPlayer

    def _possible_moves_dog(self):
        possible_moves = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 'D':
                    # Check horizontal moves to the right
                    for c in range(j+1, len(self.board[0])):
                        if self.board[i][c] is None:
                            possible_moves.append(((i, j), (i, c)))
                        else:
                            break
                    # Check horizontal moves to the left
                    for c in range(j-1, -1, -1):
                        if self.board[i][c] is None:
                            possible_moves.append(((i, j), (i, c)))
                        else:
                            break
                    # Check vertical moves up
                    for r in range(i-1, 0, -1):
                        if self.board[r][j] is None:
                            possible_moves.append(((i, j), (r, j)))
                        else:
                            break
                    # Check vertical moves down
                    for r in range(i+1, len(self.board)-1):
                        if self.board[r][j] is None:
                            possible_moves.append(((i, j), (r, j)))
                        else:
                            break
                    # Check diagonal moves up-right
                    for r, c in zip(range(i-1, 0, -1), range(j+1, len(self.board[0]))):
                        if self.board[r][c] is None:
                            possible_moves.append(((i, j), (r, c)))
                        else:
                            break
                    # Check diagonal moves up-left
                    for r, c in zip(range(i-1, 0, -1), range(j-1, -1, -1)):
                        if self.board[r][c] is None:
                            possible_moves.append(((i, j), (r, c)))
                        else:
                            break
                    # Check diagonal moves down-right
                    for r, c in zip(range(i+1, len(self.board)-1), range(j+1, len(self.board[0]))):
                        if self.board[r][c] is None:
                            possible_moves.append(((i, j), (r, c)))
                        else:
                            break
                    # Check diagonal moves down-left
                    for r, c in zip(range(i+1, len(self.board)-1), range(j-1, -1, -1)):
                        if self.board[r][c] is None:
                            possible_moves.append(((i, j), (r, c)))
                        else:
                            break

        return possible_moves


    def _possible_moves_bison(self):
        possible_moves = []
        for i in range(len(self.board)-1):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 'B' and self.board[i+1][j] == None:
                    possible_moves.append(((i, j), (i+1, j)))
        return possible_moves


    def _possible_moves_indian(self):
        possible_moves = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 'I':
                    # Check vertical moves
                    if i-1 >= 0 and self.board[i-1][j] in [None, 'B']:
                        possible_moves.append(((i, j), (i-1, j)))
                    if i+1 < len(self.board)-1 and self.board[i+1][j] in [None, 'B']:
                        possible_moves.append(((i, j), (i+1, j)))
                    # Check horizontal moves
                    if j-1 >= 0 and self.board[i][j-1] in [None, 'B']:
                        possible_moves.append(((i, j), (i, j-1)))
                    if j+1 < len(self.board[0]) and self.board[i][j+1] in [None, 'B']:
                        possible_moves.append(((i, j), (i, j+1)))
                    # Check diagonal moves
                    if i-1 >= 0 and j-1 >= 0 and self.board[i-1][j-1] in [None, 'B']:
                        possible_moves.append(((i, j), (i-1, j-1)))
                    if i-1 >= 0 and j+1 < len(self.board[0]) and self.board[i-1][j+1] in [None, 'B']:
                        possible_moves.append(((i, j), (i-1, j+1)))
                    if i+1 < len(self.board)-1 and j-1 >= 0 and self.board[i+1][j-1] in [None, 'B']:
                        possible_moves.append(((i, j), (i+1, j-1)))
                    if i+1 < len(self.board)-1 and j+1 < len(self.board[0]) and self.board[i+1][j+1] in [None, 'B']:
                        possible_moves.append(((i, j), (i+1, j+1)))
        return possible_moves


    def _possible_moves_dog_and_indian(self):
        pm = self._possible_moves_dog()
        pm = pm + self._possible_moves_indian()
        return pm
    
    def possible_moves(self):
        if self.currentPlayer == True:
            return self._possible_moves_bison()
        elif self.currentPlayer == False:
            return self._possible_moves_dog_and_indian()
        else:
            raise ValueError('Invalid player')
    
    def make_move(self, move):
        # Move the piece
        piece_type = self.board[move[0][0]][move[0][1]]
        self.board[move[0][0]][move[0][1]] = None
        self.board[move[1][0]][move[1][1]] = piece_type
        self.last_move = move
        self.currentPlayer = not self.currentPlayer
        return self.board
    
    def is_game_over(self):
        bison_moves = self._possible_moves_bison()
        val = False
        for f in self.board[6]:
            if f == 'B':
                return True
        if not bison_moves:
            val = True
        return val
    
    def get_result(self):
        if self.is_game_over():
            bison_moves = self._possible_moves_bison()
            for f in self.board[6]:
                if f == 'B':
                    return +1
                else:
                    return -1

    
    def display_board(self):
        print("   -----------------------")
        for row in range(7):
            print(row, end=" |")
            for col in range(11):
                if self.board[row][col] is None:
                    print("  ", end="")
                else:
                    print(f" {self.board[row][col]}", end="")
            print(" |")
        print("   -----------------------")