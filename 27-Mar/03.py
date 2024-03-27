import networkx as nx
import matplotlib.pyplot as plt

# Entities:
entities = ['Student', 'Class', 'Teacher', 'Lecture', 'Information']

# Relationships:
relationships = [
    ('Student', 'Class'),
    ('Class', 'Teacher'),
    ('Teacher', 'Lecture'),
    ('Lecture', 'Information'),
    ('Student', 'Information')
]

# Simple Semantic Net (Ignoring Verbs)
G_simple = nx.DiGraph()

# Adding entities as nodes
for entity in entities:
    G_simple.add_node(entity)

# Adding relationships as edges
for relationship in relationships:
    G_simple.add_edge(relationship[0], relationship[1])

# Plotting Simple Semantic Net
plt.figure(figsize=(8, 6))
plt.title("Simple Semantic Net (Entities Only) (Ingorning the Verb)")
pos = nx.spring_layout(G_simple, seed=42)
nx.draw(G_simple, pos, with_labels=True, node_color='red', node_size=3000, font_size=12, width=1.5)
plt.show()

# Reifying Verbs
reified_relationships = [
    ('Student', 'attend', 'Class'),
    ('Class', 'have', 'Teacher'),
    ('Teacher', 'provide', 'Lecture'),
    ('Lecture', 'contain', 'Information'),
    ('Student', 'study', 'Information')
]

# Reified Semantic Net
G_reified = nx.MultiDiGraph()

# Adding entities as nodes
for entity in entities:
    G_reified.add_node(entity)

# Adding reified relationships as edges
for relationship in reified_relationships:
    subject, verb, obj = relationship
    G_reified.add_edge(subject, obj, label=verb)

# Plotting Reified Semantic Net
plt.figure(figsize=(15, 5))
plt.title("Reified Semantic Net")
pos = nx.spring_layout(G_reified, seed=42)
nx.draw(G_reified, pos, with_labels=True, node_color='lightgreen', node_size=3000, font_size=12, width=1.5)
edge_labels = {(u, v): d['label'] for u, v, d in G_reified.edges(data=True)}
nx.draw_networkx_edge_labels(G_reified, pos, edge_labels=edge_labels, font_size=10)
plt.axis('off')
plt.show()
