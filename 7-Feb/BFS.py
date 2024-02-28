from collections import deque

def bfs(adj_matrix, initial_node, goal_node):
    queue = deque()
    visited = set()     # keep track of visited nodes
    initial_path = [initial_node] # initial path with the starting node
    queue.append(initial_path) 
    visited.add(initial_node)  # visited node

    while queue:
        path = queue.popleft()
        current_node = path[-1]
        if current_node == goal_node:          # Check if the current node is the goal node
            print("Optimal Path:", path)
            return
        
        print("Queue:", path, "Total Nodes:", len(path))
        for neighbour in range(1, len(adj_matrix[current_node - 1]) + 1):
            # Check if the neighbour is connected to the current node and if it's not visited
            if adj_matrix[current_node - 1][neighbour - 1] == 1 and neighbour not in visited:
                new_path = path + [neighbour]                   #new path by appending the neighbour to the current path
                queue.append(new_path) # Add the new path to the queue
                visited.add(neighbour)

    print("No path found from node", initial_node, "to node", goal_node)

if __name__ == "__main__":
    adjacent_matrix = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ]
    initial_node = 1
    # Goal node to reach
    goal_node = 5

    # Call the BFS function with the given parameters
    bfs(adjacent_matrix, initial_node, goal_node)