# Lab 8: Building a Knowledge Base as a Multigraph

## Introduction
In this lab, we will construct a simple knowledge base represented as a multigraph. A multigraph extends the concept of a graph by allowing multiple edges between nodes, each carrying different types of information. We will identify entities (nouns) and relationships from a given text paragraph, and represent them as nodes and edges respectively in the multigraph.

## Task Overview
1. Download an arbitrary paragraph from the internet containing around six sentences.
2. Identify all entities (nouns) in the paragraph, resolving any pronouns to their respective nouns.
3. Create a list of all identified entities.
4. Identify relationships between these entities.
5. Construct a multigraph with entities as nodes and relationships as edges.

## Example Multigraph Construction

### Paragraph:
"The cat sat on the mat. It purred softly as it watched the birds outside. The birds chirped happily in the tree. A squirrel scampered across the lawn. The cat's tail twitched with excitement. It longed to chase after the birds."

### Identified Entities:
- cat
- mat
- birds
- tree
- squirrel
- lawn
- tail
- excitement

### Relationships:
1. cat sat on mat
2. cat watched birds
3. birds chirped in tree
4. squirrel scampered across lawn
5. cat's tail twitched with excitement
6. cat longed to chase after birds

### Multigraph Representation:
- Nodes: cat, mat, birds, tree, squirrel, lawn, tail, excitement
- Edges:
    - cat -> mat (sat on)
    - cat -> birds (watched)
    - birds -> tree (chirped in)
    - squirrel -> lawn (scampered across)
    - cat -> tail (twitched with)
    - cat -> excitement (longed to chase after)

## Traversal Procedure
After constructing the multigraph, implement a traversal procedure that accepts a pair of nodes and returns true if there is a path from the first node to the second, otherwise false.

## Conclusion
In this lab, we have learned how to build a knowledge base using a multigraph representation. This approach allows for capturing complex relationships between entities in a structured manner. Traversal procedures further enable querying and reasoning over the knowledge base.
