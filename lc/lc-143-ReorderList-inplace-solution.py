#lc-143 Reorder List (inplace solution)


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

        fastptr = slowptr = head
        while fastptr and fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next.next

        # reverse the second half of the queue
        second_half = slowptr.next
        slowptr.next = None
        prev = None
        curr = second_half
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # merge second of half of the queue with first half
        first_half = head
        second_half = prev
        while second_half: # start moving from the last element backwards
            temp1 = first_half.next
            temp2 = second_half.next

            first_half.next = second_half
            second_half.next = temp1

            first_half = temp1
            second_half = temp2

