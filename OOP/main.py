import game as gm
import montecarlo as mc

def simulate_game():
    game = gm.Game(gm.winning_board())
    root = mc.Node(game)

    while not game.is_game_over():
        best_child = mc.monte_carlo_tree_search(root, 15000)
        game.make_move(best_child.state.last_move)
        root = mc.Node(game)
        game.display_board()
    
    result = game.get_result()
    return result

simulate_game()

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