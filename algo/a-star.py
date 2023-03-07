# Function to discover optimal path using A-star algorithm

import heapq
import math

def astar(start, goal, neighbors_fn, heuristic_fn):
    """
    Find the shortest path from start to goal using A* algorithm.
    Args:
        start: the starting node
        goal: the goal node
        neighbors_fn: a function that returns the neighbors of a given node
        heuristic_fn: a function that estimates the cost from a node to the goal
    Returns:
        The shortest path from start to goal as a list of nodes.
    """
    # Create the open and closed sets
    to_visit = []
    visited = set()

    # Initialize the start node
    heapq.heappush(to_visit, (0, start, [start]))

    while to_visit:
        # Get the node with the lowest f score
        current_f, current_node, current_path = heapq.heappop(to_visit)

        # Check if the current node is the goal
        if current_node == goal:
            return current_path

        # Add the current node to the visited set
        visited.add(current_node)

        # Iterate over the neighbors of the current node
        for neighbor in neighbors_fn(current_node):
            # Skip neighbors that are already in the visited
            if neighbor in visited:
                continue

            # Calculate the g score of the neighbor
            g_score = len(current_path)

            # Calculate the h score of the neighbor
            h_score = heuristic_fn(neighbor, goal)

            # Calculate the f score of the neighbor
            f_score = g_score + h_score

            # Check if the neighbor is already in the to visit
            visited_neighbour = True
            for i, (f, n, p) in enumerate(to_visit):
                if n == neighbor:
                    visited_neighbour = False
                    if f_score < f:
                        # Update the existing neighbor in the open set with the new path
                        to_visit[i] = (f_score, neighbor, current_path + [neighbor])
                    break

            if visited_neighbour:
                # Add the neighbor to the open set
                heapq.heappush(to_visit, (f_score, neighbor, current_path + [neighbor]))

    # If no path is found, return None
    return None


# Example usage
# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Define the heuristic function
def heuristic(node, goal):
    if node == goal:
        return 0
    else:
        return 1

# Define the start and goal nodes
start = 'A'
goal = 'F'

# Define the neighbors function
def neighbors(node):
    return graph[node]

# Find the shortest path using A star
path = astar(start, goal, neighbors, heuristic)
print(path)
