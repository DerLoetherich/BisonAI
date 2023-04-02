import game as gm
import random
from math import log,sqrt,e,inf

class Node:
    def __init__(self, state = gm.Game()):
        self.state = state
        self.children = []
        self.parent = None
        self.num_parentVisit = 0
        self.num_visit = 0
        self.exploitation_v = 0

def ucb1(curr_node):
    result = curr_node.exploitation_v+2*(sqrt(log(curr_node.num_parentVisit+e+(10e-6))/(curr_node.num_visit+(10e-10))))
    return result


def expand(node):
    moves = node.state.possible_moves()
    for move in moves:
        child_state = node.state.make_move(move)
        child_node = Node(child_state)
        child_node.parent = node
        node.children.append(child_node)

def select(node):
    while not node.state.game_over():
        if not node.children:
            # if the node has no children, it means it has not been explored yet, so return this node
            return node
        else:
            # select the child node with the highest UCB1 value
            ucb1_values = [ucb1(child_node) for child_node in node.children]
            max_ucb1_value = max(ucb1_values)
            max_ucb1_index = ucb1_values.index(max_ucb1_value)
            node = node.children[max_ucb1_index]
    
    return node  # if the current node is terminal, return it

def playout(node):
    curr_node = node
    while not curr_node.state.is_game_over():
        curr_node = expand(curr_node)
        curr_node = select(curr_node)
    result = curr_node.state.get_result()
    return result

def backpropagation(node, result):
    curr_node = node
    while curr_node is not None:
        curr_node.num_visit += 1
        curr_node.exploitation_v += result
        curr_node = curr_node.parent

def monte_carlo_tree_search(root):
    for i in range(1000):
        node = select(root)
        result = playout(node)
        backpropagation(node, result)
    best_child = max(root.children, key=lambda child: child.num_visit)
    return best_child
