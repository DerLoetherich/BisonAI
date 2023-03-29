import Game as gm
import MonteCarlo as mc

root = {
    "board": gm.starting_board(),
    "player": True,  # True represents the Bisons player, False represents the Dogs/Indian player
    "num_visits": 0,
    "total_reward": 0,
    "children": [],
}

print(mc.run_mcts(root, root['player'], 1000))