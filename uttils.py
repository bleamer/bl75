class Utils:
    def __init__(self) -> None:
        pass

    def dfs(self, G, start):
        """Depth First search using Adjacency List

        Args:
            G (List): Adjcency list describing the graph
            start (None): Starting node of the adjacency list
        """
        print('\nDFS Adjacency list')
        stack = []
        visited = [False] * len(G)
        stack.append(start)
        while(stack):
            vertex = stack.pop()
            print(vertex)
            if not visited[vertex]:
                visited[vertex] = True
                for neighbour in G[vertex]:
                    stack.append(neighbour)
    
    def dfs_mat(self, G, start):
        """Depth first search given adjacency matrix        

        Args:
            G (List(List)): 2-dim list representing node connectsions
            start (None): Starting node to traverse the graph
        """
        print('\nDFS Adjacency matrix')
        stack = []
        visited =[False] * len(G[0])
        stack.append(start)
        while stack:
            vertex = stack.pop()
            if visited[vertex] == False:
                visited[vertex] = True
                print(vertex)
                for w in range(len(G[0])):
                    if G[vertex][w] != 0:
                        stack.append(w)
    

if __name__ == '__main__':
    # Adjacency list representation of graph
    G = [[1],       # Node 0 (A) has node 1 (B) as neighbor
        [0, 6],    # Node 1 (B) has node 0 (A) and 6 (G) as neighbor
        [3],
        [2, 4, 6],
        [3, 5],
        [4, 6, 7],
        [1, 3, 5],
        [5]]    
    # Adjacency matrix
    graphx = [[1, 1, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 1, 0],
              [0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 1, 1, 1, 0, 1, 0],
              [0, 0, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 1],
              [0, 1, 0, 1, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 1, 0, 1]]
    utils = Utils()
    utils.dfs(G, 0)
    utils.dfs_mat(graphx, 0)
