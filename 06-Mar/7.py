import random

class Node:
    def __init__(self, name, depth, branching_factor):
        self.name = name
        self.depth = depth
        self.branching_factor = branching_factor
        self.children = []
        self.utility = None

node_visit_count = 0

def generate_game_tree(node):
    global node_visit_count
    node_visit_count += 1

    if node.depth == 0:
        node.utility = random.randint(-5, 5)
    else:
        for i in range(node.branching_factor):
            child_name = f"{node.name}_{i + 1}"
            child = Node(name=child_name, depth=node.depth - 1, branching_factor=node.branching_factor)
            node.children.append(child)
            generate_game_tree(child)

def minmax(node, maximizing_player=True):
    global node_visit_count
    node_visit_count += 1

    if not node.children:
        return node.utility

    if maximizing_player:
        return max(minmax(child, False) for child in node.children)
    else:
        return min(minmax(child, True) for child in node.children)

def print_game_tree(node, depth=0, last_child=False):
    prefix = "│   " * (depth - 1) + "└── " if last_child else "│   " * depth + "├── "
    print(prefix + f"{node.name} (Utility: {node.utility})")

    for i, child in enumerate(node.children):
        print_game_tree(child, depth + 1, i == len(node.children) - 1)

root = Node(name="Root", depth=3, branching_factor=4)
generate_game_tree(root)

node_visit_count = 0
minmax_result = minmax(root)

print("\nGenerated Game Tree:")
print_game_tree(root)
print("\nMINMAX Result:", minmax_result)
print("Number of Nodes Visited in MINMAX:", node_visit_count)
