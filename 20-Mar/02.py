import networkx as nx
import matplotlib.pyplot as plt

# Entity-Relationship Diagram Visualization

# Entities:
# 1. Aryan: Our diligent student.
# 2. Student: The eager learners.
# 3. Class: Hubs of knowledge.
# 4. Teacher: The guiding mentors.
# 5. Lecture: Wellsprings of wisdom.
# 6. Information: The treasure trove.

# Relationships:
# - Aryan is a student.
# - Students attend classes.
# - Classes have teachers.
# - Teachers provide lectures.
# - Lectures contain information.
# - Students delve into information.

entities = ['Aryan', 'Student', 'Class', 'Teacher', 'Lecture', 'Information']
relationships = [
    ('Aryan', 'Student', 'is a'),
    ('Student', 'Class', 'attend'),
    ('Class', 'Teacher', 'have'),
    ('Teacher', 'Lecture', 'provide'),
    ('Lecture', 'Information', 'contain'),
    ('Student', 'Information', 'study')
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

nx.draw(G, pos, with_labels=True, 
        node_color='lightgreen', 
        node_size=1500, 
        font_size=10, 
        width=2,
        edge_color='gray',
        arrowsize=10)

edge_labels = {(u, v): d['label'] 
                for u, v, d in G.edges(data=True)}

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.title("Entity Relationship Diagram", fontsize=16)  
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.axis('off')  # Turn off axis
plt.show()
