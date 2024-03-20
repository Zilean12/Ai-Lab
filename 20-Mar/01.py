import networkx as nx
import matplotlib.pyplot as plt

# Entities and relationships
entities = ['Alice', 'student', 'class', 'teacher', 'lecture', 'information']
relationships = [
    ('Alice', 'student', 'is a'),
    ('student', 'class', 'attend'),
    ('class', 'teacher', 'have'),
    ('teacher', 'lecture', 'provide'),
    ('lecture', 'information', 'contain'),
    ('student', 'information', 'study')
]

# Creating a multigraph
G = nx.MultiDiGraph()

# Adding the nodes
for entity in entities:
    G.add_node(entity)

# Adding the edges
for relationship in relationships:
    G.add_edge(relationship[0], relationship[1], label=relationship[2])

# Drawing the graph
plt.figure(figsize=(10, 6))  # Set the figure size
pos = nx.spring_layout(G, seed=42)  # Seed for reproducibility
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=10, width=1.5, edge_color='gray', arrowsize=10)
edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
plt.title("Entity Relationship Diagram", fontsize=16)  # Add a title
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.axis('off')  # Turn off axis
plt.show()
