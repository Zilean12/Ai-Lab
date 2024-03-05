# Breadth-First Search (BFS) on Graph

---

## 🌐 Overview

Welcome to the Breadth-First Search (BFS) on Graph assignment! In this task, you'll be implementing the BFS algorithm on a graph using Python. This implementation will accept an adjacency matrix representing the graph, along with initial and goal nodes. Throughout the BFS process, the program will output the nodes present in the BFS queue and the total number of nodes at each stage. Finally, it will print the optimal path from the initial to the goal nodes.

## 📋 Requirements

To successfully complete this assignment, ensure that your Python program meets the following requirements:

- Implement BFS on a graph using an adjacency matrix representation.
- Accept any node as the initial and goal nodes.
- Output the node lists present in the BFS queue at each stage.
- Output the total number of nodes in the queue at each stage.
- Print the optimal path from the initial to the goal nodes.

## 📝 Pseudocode

Here's a high-level overview of the BFS algorithm:

1. Create a queue to store paths, initialized with the first path starting from the initial state.
2. While the queue is not empty:
   - Get the frontmost path from the queue.
   - Check if the last node of this path is the goal node:
     - If true, print the optimal path.
   - For each connected neighbor of the current node:
     - If the neighbor is not visited, create a new path by appending it to the current path and add it to the queue.

## 🚀 Instructions

1. Clone the repository.
2. Ensure you have Python installed.
3. Open your preferred Python environment and execute the provided `BFS.py` file.
4. Follow the prompts to input the adjacency matrix, initial node, and goal node.
5. View the output to observe the nodes present in the BFS queue, the total number of nodes in the queue at each stage, and the optimal path from the initial to the goal nodes.

## 🤝 Contributions

Contributions are welcome! If you have any improvements or bug fixes, feel free to submit a pull request.

---

*This README provides an overview, instructions, and guidelines for the Breadth-First Search (BFS) implementation on a graph assignment. Your success is our priority!* 🌟
