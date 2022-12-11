# blind list 75 - 59 : Graph valid treee
# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

from typing import (
    List,
)

from collections import defaultdict

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def isCyclic(G, start, n):
        """isCyclic utility method to check if the given graph is cyclic or not


        Arguments:
            G -- Adjacency list describing the graph
            start -- first node to start checking from
            n - No. of nodes
        """ 


        if  not G:
            return True
        visited = [False] * len(n)
        stack = []
        stack.append(start)
        while stack:
            vertex = stack.pop()
            if visited[vertex]:
                return True # Visited earlier, visiting again ->  Graph is cyclic 
            else:
                visited[vertex] = True
                for w in G[vertex]:
                    stack.append(w)
                    
        return False  # Never revisited a node graph acyclic

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # is not cyclic
        # is all connected
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)


        visited = set()
        def dfs(i, prev, aList):
            if i in visited:
                return False
            
            visited.add(i)
            for j in aList[i]:
                if j == prev:
                    continue
                if not dfs(j, i, aList):
                    return False
            return True


        return dfs(0, -1, adjList) and n == len(visited)

    


solution = Solution()
print(solution.valid_tree(n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 3]]))
print(solution.valid_tree(n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4],]))

