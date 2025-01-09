#973. K Closest Points to Origin
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_heap = []
        for x, y in points:
            heapq.heappush(dist_heap, (x**2 + y**2, (x,y)))
        # print(dist_heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(dist_heap)[1])

        return res