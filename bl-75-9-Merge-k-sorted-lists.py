# bl-75-9-Merge-k-sorted-lists Solution
# lc-23


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #initialize current pointer for lists
        sNode = resList = ListNode(0,None)
        pq = []
        cur = [lst for lst in lists]
        for idx, lst in enumerate(cur):
            if lst:
                print((lst.val, (lst, idx)))
                heapq.heappush(pq, [lst.val, idx, lst])
        while pq:
            val, idx, lst = heapq.heappop(pq)
            resList.next = lst
            resList = resList.next
            cur[idx] = cur[idx].next
            if cur[idx]:
                heapq.heappush(pq, [cur[idx].val, idx, cur[idx]])
        return sNode.next