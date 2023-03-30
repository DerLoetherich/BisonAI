import Game as gm
import MonteCarlo as mc
import simulation as sim
import math

root = {
    "board": gm.starting_board(),
    "player": True,  # True represents the Bisons player, False represents the Dogs/Indian player
    "num_visits": 0,
    "total_reward": 0,
    "children": [],
    "move": None,  # The root node has no move
}


#print(mc.run_mcts(root, root['player'], 1000))

sim.play_game()
#print(root["board"])
#mc.run_mcts(root, root["player"], 100)
#best_child = mc.ucb1_select_child(root)
#print(best_child["move"])
#print(root["board"])
#board = gm.move_piece(best_child["move"], root["board"])
#print(board)