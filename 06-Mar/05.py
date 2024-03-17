import random

class Node:

    def __init__(self, value=None):
        self.value = value
        self.children = []

    # Generate a game tree with depth and maximum number of children.
    def generating_game_tree(self, depth, max_children):
        if depth == 0:
            return Node(random.randint(-5, 5))
        
        # Otherwise, create a non-leaf node
        node = Node()
        num_children = random.randint(1, max_children)  # Adjusted range to ensure at least one child
        for i in range(num_children):
            # Recursively generate children nodes
            node.children.append(node.generating_game_tree(depth - 1, max_children))
        return node

    # minmax node
    def evaluate(self, node, is_maximizing_player):
        if not node.children:         # If the node is a leaf, return its value
            return node.value
    
        if is_maximizing_player:
            best_value = float('-inf')         # If the current player is maximizing, the best move value as negative
            for child in node.children:
                best_value = max(best_value, self.evaluate(child, False))    # Recursively evaluate children nodes with the opposing player's turn
            return best_value
        else:
            # if the current player is minizing, the best move and value may be postive
            best_value = float('inf')
            for child in node.children:
                best_value = min(best_value, self.evaluate(child, True))
            return best_value
        
    # printing the generated tree
    def print_tree(self, node, is_maximizing_player, depth=0):
        node_type = "MAX Value" if is_maximizing_player else "MIN"
        print (" | " * depth + f"{node_type} node: {node.value}")
        if node.children:
            for child in node.children:
                self.print_tree(child, not is_maximizing_player, depth + 1)

# defining the depth, max_children
depth = 3
max_children = 2
root_node = Node().generating_game_tree(depth, max_children)

# Printing the MinMAx Tree 
print("Generated Game Tree Structure:")
root_node.print_tree(root_node, True)

# printing the best move and optimited move 
minimax_value = root_node.evaluate(root_node, True)
print("\nMinimax without alpha-beta pruning:")
print("Best choice:", minimax_value)