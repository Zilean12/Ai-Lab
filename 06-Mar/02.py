import random

class Node:
    def __init__(self, name=None, utility=None):
        self.name = name
        self.utility = utility
        self.children = []

def generate_game_tree(node, depth, count=[1]):
    node.name = f"Node {count[0]}"
    count[0] += 1
    
    if depth == 0:
        node.utility = random.randint(-5, 5)
        return
    for i in range(random.randint(3, 4)):
        child = Node()
        node.children.append(child)
        generate_game_tree(child, depth - 1, count)

def minmax(node, maximizing_player=True, depth=0):
    if not node.children:
        print(f"Visited Node - Depth: {depth}, {node.name} (Utility: {node.utility})")
        return node.utility
    
    value = float('-inf') if maximizing_player else float('inf')
    
    for child in node.children:
        child_value = minmax(child, not maximizing_player, depth + 1)
        value = max(value, child_value) if maximizing_player else min(value, child_value)
    
    return value

# Generate a game tree of depth 'd'
depth = 3
root = Node()
generate_game_tree(root, depth)

# Apply MINMAX Algorithm
optimal_choice_minmax = minmax(root)
print("Best move using MINMAX Algorithm:", optimal_choice_minmax)
