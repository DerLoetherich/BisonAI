import Game as gm
import random
import math
import copy

C=1.41 # Exploration constant
EPSILON = 1e-8 
MAX_TERM = 1e100

def get_random_move(board, player):
    possible_moves = gm.possible_moves_bison(board) if player == True else gm.possible_moves_dog_and_indian(board)
    move = random.choice(possible_moves)
    return move

def get_reward(board, player):
    winner, _ = gm.game_over(board)
    if winner is None:
        return 0
    elif winner == 'B' and not player or winner == 'W' and player:
        return -1
    else:
        return 1

def simulate_random_game(board, player):
    while not gm.game_over(board)[0]:
        move = get_random_move(board, player)
        board = gm.move_piece(move, board)
        player = not player
    _, winner = gm.game_over(board)
    if winner == 'B':
        return 1 if player else -1
    elif winner == 'I':
        return 1 if not player else -1
    

def ucb1_select_child(node):
    """
    Selects a child node based on the UCB1 formula.
    """
    best_score = -1
    best_child = None
    for child in node["children"]:
        exploitation_term = child["total_reward"] / child["num_visits"]
        exploration_term = math.sqrt(2 * math.log(node["num_visits"]) / child["num_visits"])
        ucb1_score = exploitation_term + exploration_term
        if ucb1_score > best_score:
            best_score = ucb1_score
            best_child = child
    return best_child


def get_reward(board, player):
    winner = gm.check_winner(board)
    if winner == player:
        return 1
    else:
        return -1


def run_mcts_iteration(root, player):
    """
    Runs one iteration of Monte Carlo Tree Search starting from the root node.
    """
    node = root
    path = []

    # Select a leaf node to expand
    while node["children"]:
        # Use the UCB1 formula to select the best child node
        child = ucb1_select_child(node)
        path.append((node, child))
        node = child

    # Expand the selected leaf node by adding one of its unexplored children
    unexplored_moves = [move for move in gm.possible_moves(node['board'], node['player']) if move not in node['children']]
    if unexplored_moves:
        # Choose a random unexplored move
        move = random.choice(unexplored_moves)
        new_board = gm.move_piece(move[0], move[1], node["board"])
        new_node = {
            "board": new_board,
            "player": -player,
            "num_visits": 0,
            "total_reward": 0,
            "children": [],
        }
        node["children"].append(new_node)
        path.append((node, new_node))
        node = new_node

    # Simulate a game from the newly added node
    reward = get_reward(node["board"], player)

    # Update the statistics for all nodes in the path
    for parent, child in path:
        child["num_visits"] += 1
        child["total_reward"] += reward * (1 if child["player"] == player else -1)



        
print(simulate_random_game(gm.starting_board(), True))