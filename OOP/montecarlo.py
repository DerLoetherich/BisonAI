import game as gm
import random
import time
import copy
from math import log,sqrt,e,inf

C = sqrt(2) # Exploration Weight

class Node:
    def __init__(self, state = gm.Game()):
        self.state = state
        self.children = []
        self.parent = None
        self.num_visit = 0
        self.total_reward = 0

    def is_fully_expanded(self):
        return len(self.get_unexplored_moves()) == 0
        
    def get_unexplored_moves(self):
        explored_moves = [child.state.last_move for child in self.children]
        all_moves = self.state.possible_moves()
        unexplored_moves = [move for move in all_moves if move not in explored_moves]
        return unexplored_moves
        
    def add_child(self, node):
        self.children.append(node)
        node.parent = self


def uct(curr_node):
    if curr_node.num_visit == 0:
        return float('inf')  # if node has not been visited, return infinity to encourage its selection
     
    exploitation_value = curr_node.total_reward / curr_node.num_visit
    exploration_value = C * sqrt(log(curr_node.parent.num_visit+(10e-6)) / (curr_node.num_visit+(10e-10)))
    uct_value = exploitation_value + exploration_value
    return uct_value

def expand(node):
    unexplored_moves = node.get_unexplored_moves()
    move = random.choice(unexplored_moves)
    child_state = copy.deepcopy(node.state)
    new_state = gm.Game(child_state.make_move(move))
    new_node = Node(new_state)
    node.add_child(new_node)
    return new_node

def select(node):
    while not node.state.is_game_over():
        if not node.is_fully_expanded():
            return expand(node)
        else:
            uct_values = [uct(child_node) for child_node in node.children]
            max_uct_index = max(range(len(uct_values)), key=uct_values.__getitem__)
            node = node.children[max_uct_index]
    return node

def rollout(node):
    while not node.state.is_game_over():
        move = random.choice(node.state.possible_moves())
        node.state.make_move(move)
    return node.state.get_result()

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
    best_child = max(root.children, key=lambda child: (child.total_reward/(child.num_visit + 10e-10)))
    print("Duration:")
    print(time.time() - start_time)
    return best_child

def print_attributes(object):
    attributes = vars(object)
    for attribute, value in attributes.items():
        print(attribute, "=", value)