# LC743. Network Delay Time (Djikstra's alogrithm)

from collections import deque
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))

        minHeap = [(0,k)]
        visited = set()
        cost = 0 # Cost to reach the farthest node so far 
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            cost = max(cost, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w2 + w1, n2))

        return cost if len(visited) == n else -1