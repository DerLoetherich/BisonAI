import game as gm
import random
import time
import copy
from math import log,sqrt,e,inf

C = sqrt(2) # Exploration Weight

class Node:
    def __init__(self, state = gm.Game(), move = None):
        self.state = state
        self.children = []
        self.parent = None
        self.num_parentVisit = 0
        self.num_visit = 0
        self.exploitation_value = 0
        self.total_reward = 0

def uct(curr_node):
    if curr_node.num_visit == 0:
        return float('inf')  # if node has not been visited, return infinity to encourage its selection
    if curr_node.state.currentPlayer == True:
        exploitation_value = curr_node.total_reward / curr_node.num_visit
        exploration_value = C * sqrt(log(curr_node.parent.num_visit+(10e-6)) / (curr_node.num_visit+(10e-10)))
        uct_value = exploitation_value + exploration_value
    else:
        exploitation_value = -1*(curr_node.total_reward) / curr_node.num_visit
        exploration_value = C * sqrt(log(curr_node.parent.num_visit+(10e-6)) / (curr_node.num_visit+(10e-10)))
        uct_value = exploitation_value + exploration_value  
    return uct_value


def expand(node):
    moves = node.state.possible_moves()
    for move in moves:
        child_state = copy.deepcopy(node.state)
        child_state.make_move(move)
        child_node = Node(child_state)
        child_node.parent = node
        child_node.num_parentVisit = node.num_visit
        node.children.append(child_node)

def select(node):
    while not node.state.is_game_over():
        if not node.children:
            # if the node has no children, it means it has not been explored yet, so expand it
            expand(node)
            # select a random child node
            node = random.choice(node.children)
        else:
            # select the child node with the highest uct value
            uct_values = [uct(child_node) for child_node in node.children]
            max_uct_value = max(uct_values)
            max_uct_index = uct_values.index(max_uct_value)
            node = node.children[max_uct_index]
    
    return node  # return a random child node if the current node is terminal

def playout(node):
    curr_node = node
    while not curr_node.state.is_game_over():
        if not curr_node.children:
            # if the node has no children, it means it has not been explored yet, so expand it
            expand(curr_node)
            # select a random child node to explore
            curr_node = random.choice(curr_node.children)
        else:
            # select the child node with the highest UCT value
            uct_values = [uct(child_node) for child_node in curr_node.children]
            max_uct_value = max(uct_values)
            max_uct_index = uct_values.index(max_uct_value)
            curr_node = curr_node.children[max_uct_index]
        # increment the visit count of the selected child node
        curr_node.num_visit += 1
        
    result = curr_node.state.get_result()
    return result


def backpropagation(node, result):
    curr_node = node
    while curr_node is not None:
        curr_node.num_visit += 1
        curr_node.total_reward += result
        curr_node = curr_node.parent


def monte_carlo_tree_search(root, num_iterations):
    start_time = time.time()
    for i in range(num_iterations):
        node = select(root)
        result = playout(node)
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