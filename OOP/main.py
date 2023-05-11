import game as gm
import montecarlo as mc
import copy

def self_play(num_iterations):
    # initialize game and root node
    game = gm.Game(gm.winning_board(), False)
    root = mc.Node(game)
    game.display_board()

    while not game.is_game_over():
        best_child = mc.monte_carlo_tree_search(root, num_iterations)
        game.make_move(best_child.state.last_move)
        root = mc.Node(copy.deepcopy(game))
        game.display_board()

    result = game.get_result()
    return result

self_play(5000)

#game = gm.Game(gm.winning_board(), False)
#root = mc.Node(game)

#best_child = mc.monte_carlo_tree_search(root, 2)
#print(best_child.state.last_move)
#game.display_board()





"""
game = gm.Game()
root = mc.Node(game)
#mc.expand(root)
print(game.possible_moves())
best_child = mc.monte_carlo_tree_search(root, 50)
mc.print_attributes(best_child.state)
game.make_move(best_child.state.last_move)
root = mc.Node(game)
game.display_board()
print(game.possible_moves())
best_child = mc.monte_carlo_tree_search(root, 50)
mc.print_attributes(best_child.state)
game.make_move(best_child.state.last_move)
root = mc.Node(game)
game.display_board()
"""

"""
one = mc.monte_carlo_tree_search(root, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
one = mc.monte_carlo_tree_search(two, 5000)
two = mc.monte_carlo_tree_search(one, 5000)
"""




#simulate_game()