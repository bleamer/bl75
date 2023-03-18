# bl75-8-Merge-2-Sortedlists Solution
#lc-21

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2
        head = res = ListNode(0, None)
        while cur1 and cur2:
            if cur1.val < cur2.val:
                res.next = cur1
                cur1 = cur1.next
            else:
                res.next = cur2
                cur2 = cur2.next
            res = res.next
        if not cur2:
            res.next = cur1
        else:
            res.next = cur2
        return head.next