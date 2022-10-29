# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = l1
        y = l2
        if x is None:
            return x
        if y is None:
            return y
        carry = 0
        start = ListNode()
        node = start
        while x and y:
            val = x.val + y.val + carry
            if val > 9:
                carry = 1
                val = val -10
            else:
                carry = 0
            node.val = val
            if x.next or y.next:
                node.next = ListNode()
                node = node.next
            x = x.next
            y = y.next
        
        while x:
            val = x.val + carry
            if val > 9:
                carry = 1
                val = val -10
            else:
                carry = 0
            node.val = val
            if x.next:
                node.next = ListNode()
                node = node.next
            x = x.next
        while y:
            val = y.val + carry
            if val > 9:
                carry = 1
                val = val -10
            else:
                carry = 0
            node.val = val
            if y.next:
                node.next = ListNode()
                node = node.next
            y = y.next
        if carry == 1:
            node.next = ListNode(1)
            
        return start
            
        
        
                
                
            