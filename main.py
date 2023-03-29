import Game as gm
import MonteCarlo as mc

root = mc.create_node(gm.starting_board(), 'B')
for i in range(100):
    mc.run_mcts_iteration(root, gm.starting_board())
    i += 1

print(mc.select_best_move(root))