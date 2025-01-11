#lc-143 Reorder List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return


        queue = deque()
        ptr = head
       
        while ptr:
            queue.append(ptr)
            ptr = ptr.next

        current = queue.popleft()
        flag = True
        while queue:
            if flag:
                current.next = queue.pop()
            else:
                current.next = queue.popleft()
            current = current.next
            flag = not flag
        current.next = None