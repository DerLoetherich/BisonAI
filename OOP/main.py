import bison as bn
import montecarlo as mc
import copy

def self_play(num_iterations):
    # initialize game and root node
    root = mc.Node(bn.board())
    display_state = bn.board()
    bn.display_board(root.state)

    while not bn.is_game_over(root.state):
        best_child = mc.monte_carlo_tree_search(root, num_iterations)
        display_state = bn.make_move(display_state, best_child.last_move)
        root = best_child
        bn.display_board(display_state)

    result = bn.get_result(root.state)
    return result

self_play(20000)