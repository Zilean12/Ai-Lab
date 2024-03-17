import random
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def generate_game_tree(node, depth):
    if depth == 0:
        node.value = random.randint(-5, 5)
        return
    for _ in range(random.randint(3, 4)):
        child = Node()
        node.children.append(child)
        generate_game_tree(child, depth - 1)

def visualize_game_tree(node, graph=None, parent_name=None, pos=None, level=0, width=1.):
    if graph is None:
        graph = nx.DiGraph()
    if pos is None:
        pos = {node: (0, 0)}
    else:
        pos[node] = (level, width)
    graph.add_node(node, label=f"{node.value}\nLevel {level}")
    if parent_name is not None:
        graph.add_edge(parent_name, node)
    width += 1 / 2.0
    for child in node.children:
        pos, width = visualize_game_tree(child, graph=graph, parent_name=node, pos=pos, level=level + 1, width=width)
    return pos, width

def main():
    # Generate a game tree of depth 'd'
    d = 3
    root = Node()
    generate_game_tree(root, d)

    # Visualize the game tree
    graph = nx.DiGraph()
    pos, _ = visualize_game_tree(root, graph=graph)
    
    # Simple plot
    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos=pos, with_labels=True, node_size=800, node_color='skyblue', font_size=8, font_color='black')
    
    plt.title('Game Tree Visualization', fontsize=12, fontweight='bold')
    plt.show()

    # MINMAX Algorithm
    optimal_choice_minmax = minmax(root)
    print("Best move using MINMAX Algorithm:", optimal_choice_minmax)

if __name__ == "__main__":
    main()
