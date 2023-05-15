import bison as bn
import random
import time
import copy
from math import log,sqrt

C = sqrt(2) # Exploration Weight

class Node:
    def __init__(self, state = bn.board(), current_player = True, last_move = None):
        self.state = state
        self.current_player = current_player
        self.last_move = last_move
        self.children = []
        self.parent = None
        self.num_visit = 0
        self.total_reward = 0

    def is_fully_expanded(self):
        return len(self.get_unexplored_moves()) == 0
        
    def get_unexplored_moves(self):
        explored_moves = [child.last_move for child in self.children]
        all_moves = bn.possible_moves(self.state, self.current_player)
        unexplored_moves = [move for move in all_moves if move not in explored_moves]
        return unexplored_moves
        
    def add_child(self, node):
        self.children.append(node)
        node.parent = self


def uct(node):
    if node.num_visit == 0:
        return float('inf')  # if node has not been visited, return infinity to encourage its selection
     
    exploitation_value = node.total_reward / node.num_visit
    exploration_value = C * sqrt(log(node.parent.num_visit+(10e-6)) / (node.num_visit+(10e-10)))
    uct_value = exploitation_value + exploration_value
    return uct_value

def expand(node):
    unexplored_moves = node.get_unexplored_moves()
    move = random.choice(unexplored_moves)
    child_state = copy.deepcopy(node.state)
    new_state = bn.make_move(child_state, move)
    new_child = Node(new_state, not node.current_player, move)
    node.add_child(new_child)
    return new_child

def select(node):
    while not bn.is_game_over(node.state):
        if not node.is_fully_expanded():
            return expand(node)
        else:
            uct_values = [uct(child_node) for child_node in node.children]
            max_uct_index = max(range(len(uct_values)), key=uct_values.__getitem__)
            node = node.children[max_uct_index]
    return node

def rollout(node):
    state = copy.deepcopy(node.state)
    current_player = node.current_player
    while not bn.is_game_over(state):
        move = random.choice(bn.possible_moves(state, current_player))
        state = bn.make_move(state, move)
        current_player = not current_player
    return bn.get_result(state)

def backpropagation(node, result):
    while node is not None:
        node.num_visit += 1
        node.total_reward += result
        node = node.parent

def monte_carlo_tree_search(root, num_iterations):
    start_time = time.time()
    for i in range(num_iterations):
        node = select(root)
        result = rollout(node)
        backpropagation(node, result)
        if i % 1000 == 0:
            print(i)
    if root.current_player:
        best_child = max(root.children, key=lambda child: (child.total_reward/(child.num_visit + 10e-10)))
    else:
        best_child = min(root.children, key=lambda child: (child.total_reward/(child.num_visit + 10e-10)))
    print("Duration:")
    print(time.time() - start_time)
    return best_child

def print_attributes(object):
    attributes = vars(object)
    for attribute, value in attributes.items():
        print(attribute, "=", value)