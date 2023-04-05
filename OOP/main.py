import game as gm
import montecarlo as mc

def simulate_game():
    game = gm.Game()
    root = mc.Node(game)

    while not game.is_game_over():
        best_child = mc.monte_carlo_tree_search(root, 1000)
        game.make_move(best_child.state.last_move)
        root = mc.Node(game)
        game.display_board()
    
    result = game.get_result()
    return result

simulate_game()