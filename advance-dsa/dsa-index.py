from collections import deque


""" 
1. Graph Representation in Python
Graphs can be represented using:

Adjacency List (Efficient for sparse graphs)
Adjacency Matrix (Efficient for dense graphs)
Adjacency List Representation (Using Dictionary)
"""

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}


# 2. Breadth-First Search (BFS)
# BFS explores all neighbors before moving to the next level. It uses a queue (FIFO structure).
# BFS Implementation



def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])  # Add unvisited neighbors

# Example
bfs(graph, 'D')  # Output: A B C D E F G H
