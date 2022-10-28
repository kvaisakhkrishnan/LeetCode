# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        x = head
        y = head.next
        z = y.next
        while z is not None:
            y.next = x
            x = y
            y = z
            z = z.next
        y.next = x
        head.next = None
        head = y
        return head
        
        