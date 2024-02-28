import networkx as nx
import matplotlib.pyplot as plt

# Read input from file
with open('input.txt', 'r') as f:
    # Read the number of variables
    n_v = int(f.readline().strip())
    
    # Create domains for each variable
    domains = {name: set(range(1, int(size) + 1)) for name, size in [f.readline().strip().split() for _ in range(n_v)]}
    
    # Read the number of unary constraints
    n_uc = int(f.readline().strip())
    
    # Read unary constraints into a list
    un_cons = [f.readline().strip() for _ in range(n_uc)]
    
    # Create a modified domains copy
    mod_domains = domains.copy()
    
    # Read the number of binary constraints
    n_bc = int(f.readline().strip())
    
    # Create labels for binary constraints
    labels = {(var1, var2): f"{var1} {op} {var2} {arith_op} {int(value)}" for var1, op, var2, arith_op, value in [f.readline().strip().split() for _ in range(n_bc)]}

# Create a graph
G = nx.Graph()
G.add_edges_from(labels.keys(), label="")

# Modify domains based on unary constraints
for constraint in un_cons:
    var, op, value = constraint.split()
    value = int(value)
    
    # Apply unary constraint
    if op == '<':
        mod_domains[var] = set(x for x in mod_domains[var] if x < value)
    elif op == '>':
        mod_domains[var] = set(x for x in mod_domains[var] if x > value)
    elif op == '<=':
        mod_domains[var] = set(x for x in mod_domains[var] if x <= value)
    elif op == '>=':
        mod_domains[var] = set(x for x in mod_domains[var] if x >= value)
    elif op == '==':
        mod_domains[var] = {value}

# Display original and modified domains
print("Original Domains:", domains)
print("Modified Domains:", mod_domains)

# Visualize the graph with a circular layout
pos = nx.circular_layout(G)
plt.figure()
nx.draw(G, pos, with_labels=True, font_color='black', node_size=500, node_color='pink', edge_color='black', width=1, alpha=0.9, labels={node: node for node in G.nodes()})
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
plt.show()
