# Topological Sort

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        print(f'initializing {self.V}')

    def addEdge(self, u, v):
        self.graph[u].append(v)
        print(f'Added edge {u}->{v}')

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        print(f'Visiting {v}')
        for i in self.graph[v]:
            if not visited[v]:
                self.topologicalSortUtil(i, visited, stack)
        
        # Push the current vertex to the stack
        print(f'appending {v}')
        stack.append(v) 
        

    def topologicalSort(self):
        # Mark all vertics as not visited
        visited = [False] * self.V
        stack = []

        # For all vertices in the graph call topoological sort
        for v in range(self.V):
            if not visited[v]:
                self.topologicalSortUtil(v, visited, stack)

        print(stack[::-1])

if __name__ == '__main__':
    g = Graph(6)

    g.addEdge(5, 2)
    g.addEdge(5, 3)
    g.addEdge(4, 3)
    g.addEdge(4, 1)
    g.addEdge(2, 0)
    g.addEdge(0, 1)
    print("Following is a Topological Sort of the given graph")
    # Function Call
    g.topologicalSort()