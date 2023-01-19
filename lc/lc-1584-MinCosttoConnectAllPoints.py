# LC 1584. Min Cost to Connect All Points


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # Build an adjacency list storing distance between any two points
        adj = { i:[] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1- y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        minCost = 0 # min total cost to span the graph
        visited = set() # if we have visited a node
        minH =[[0,0]] # [cost, point] point with minimum cost to visit next
        while len(visited) < N:  #if we have not visited all nodes
            cost, p = heapq.heappop(minH) # get the node point with least cost
            if p in visited:
                continue
            minCost += cost
            visited.add(p) # indicate current node visited
            for ncost, n in adj[p]: # for all neighbours of this node
                if n not in visited: # if we have not visited the neighbour
                    heapq.heappush(minH, [ncost, n]) # add neighboure to our sorteed list
        return minCost
