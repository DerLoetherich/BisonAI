import Game as gm
import MonteCarlo as mc

def play_game():
    # Initialize the game
    board = gm.starting_board()
    player = True  # True represents the Bisons player, False represents the Dogs/Indian player
    gm.print_board(board)

    while not gm.game_over(board)[0]:
        # Perform MCTS iterations for the current player
        root = {
            "board": board,
            "player": player,
            "num_visits": 0,
            "total_reward": 0,
            "children": [],
            "move": None
        }
        for i in range(1000):
            mc.run_mcts_iteration(root, player)

        # Select the best move according to the MCTS results
        best_child = mc.ucb1_select_child(root)
        best_move = best_child["move"]
        
        # Make the selected move
        gm.print_board(board)
        board = gm.move_piece(best_move, board)
        player = not player

    # Determine the winner of the game
    _, winner = gm.game_over(board)
    if winner == True:
        print("Bisons player wins!")
    elif winner == False:
        print("Dogs/Indian player wins!")
    else:
        print("The game ended in a tie.")
