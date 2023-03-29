import Game as gm
import MonteCarlo as mc
import math

root = {
    "board": gm.starting_board(),
    "player": True,  # True represents the Bisons player, False represents the Dogs/Indian player
    "num_visits": 0,
    "total_reward": 0,
    "children": [],
    "move": None,  # The root node has no move
}


print(mc.run_mcts(root, root['player'], 1000))