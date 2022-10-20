# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return
        while head and head.val == val:
            head = head.next
        if head is None:
            return
        x = head
        y = head.next
        
        while y is not None:
            print(x.val,y.val)
            if y.val == val:
                x.next = y.next
                y = y.next
            else:
                x = x.next
                y = y.next
        return head
        
        