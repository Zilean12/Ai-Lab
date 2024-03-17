import random

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def generate_game_tree(node, depth):
    if depth == 0:
        node.value = random.randint(-5, 5)
        return
    for _ in range(random.randint(3, 5)):
        child = Node()
        node.children.append(child)
        generate_game_tree(child, depth - 1)

# Generate a game tree of depth 'd'
d = 3
root = Node()
generate_game_tree(root, d)

# MINMAX Algorithm
def minmax(node, maximizing_player=True):
    if not node.children:
        return node.value
    
    value = float('-inf') if maximizing_player else float('inf')
    for child in node.children:
        value = max(value, minmax(child, not maximizing_player)) if maximizing_player else min(value, minmax(child, not maximizing_player))
    return value

# Assuming the root node is a MAX node
optimal_choice_minmax = minmax(root)
print("Best move using MINMAX Algorithm:", optimal_choice_minmax)

# Count nodes visited
def count_nodes(node):
    count = 1
    for child in node.children:
        count += count_nodes(child)
    return count

nodes_visited_minmax = count_nodes(root)
print("Number of nodes explored (MINMAX):", nodes_visited_minmax)

# Alpha-Beta Pruning
def alpha_beta(node, alpha, beta, maximizing_player=True):
    if not node.children:
        return node.value
    
    value = float('-inf') if maximizing_player else float('inf')
    for child in node.children:
        value = max(value, alpha_beta(child, alpha, beta, not maximizing_player)) if maximizing_player else min(value, alpha_beta(child, alpha, beta, not maximizing_player))
        alpha = max(alpha, value) if maximizing_player else min(alpha, value)
        if alpha >= beta:
            break
    return value

# Assuming the root node is a MAX node
optimal_choice_ab = alpha_beta(root, float('-inf'), float('inf'))
print("Best move using Alpha-Beta Pruning:", optimal_choice_ab)

# Count nodes visited with alpha-beta pruning
def count_nodes_ab(node, alpha, beta, maximizing_player=True):
    count = 1
    for child in node.children:
        count += count_nodes_ab(child, alpha, beta, not maximizing_player)
    return count

nodes_visited_ab = count_nodes_ab(root, float('-inf'), float('inf'))
print("Number of nodes explored (Alpha-Beta Pruning):", nodes_visited_ab)
