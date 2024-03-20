import networkx as nx
import matplotlib.pyplot as plt

# Define the sentences
sentences = [
    "The black cat stealthily stalked the white rabbit.",
    "Cats enjoy batting at small objects.",
    "Rabbits are herbivores, nibbling on fresh greens in the garden.",
    "The cat's eyes gleamed with anticipation as it approached the rabbit.",
    "Rabbits thump their hind legs as a warning signal to other rabbits.",
    "The cat's tail swished back and forth, ready to pounce on the unsuspecting rabbit."
]

# Extract the entities and relationships
entities = {"cat", "rabbit", "objects", "instincts", "herbivores", "greens", "eyes", "tail", "hind legs"}
relationships = {"stalked", "enjoy batting at", "mimicking", "nibbling on", "gleamed with anticipation",
                 "approached", "thump their hind legs as a warning signal", "swished back and forth", "ready to pounce on"}

# Create a multigraph
G = nx.MultiDiGraph()

# Add nodes and edges to the multigraph
for sentence in sentences:
    for relationship in relationships:
        if relationship in sentence:
            nodes = sentence.replace(".", "").split(relationship)
            nodes = [node.strip() for node in nodes]
            for node in nodes[:-1]:
                G.add_node(node)
            G.add_edge(nodes[0], nodes[-1], label=relationship)

# Define a function to check if a path exists between two nodes
def path_exists(G, node1, node2):
    if node1 in G and node2 in G:
        return nx.has_path(G, node1, node2)
    else:
        return False

# Check if a path exists between two nodes
print(path_exists(G, 'cat', 'rabbit'))

# Visualize the multigraph
pos = nx.circular_layout(G)  # Use circular layout

# Node and edge styling
node_size = 1500
edge_width = 2
edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
node_color = 'lightgreen'
edge_color = 'gray'

# Plotting
plt.figure(figsize=(10, 6))  # Adjust figure size
nx.draw(G, pos, with_labels=True, node_size=node_size, node_color=node_color, edge_color=edge_color, width=edge_width)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)
plt.title("Relationships between Entities")
plt.axis('off')
plt.tight_layout()  # Adjust layout for better spacing
plt.show()
