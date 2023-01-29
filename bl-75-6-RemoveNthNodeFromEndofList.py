# bl-75-6 Remove Nth Node From End of List

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0, head)
        left = start
        right = head 
        count  = n
        while count > 0 and right:
            right = right.next
            count -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return start.next

