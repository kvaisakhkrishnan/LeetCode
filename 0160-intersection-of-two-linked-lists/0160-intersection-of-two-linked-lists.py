# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        x = 0
        a = headA
        while a is not None:
            x+=1
            a=a.next
        y = 0
        b = headB
        while b is not None:
            y+=1
            b = b.next
        if x < y:
            while x < y:
                headB = headB.next
                x+=1
        else:
            while y < x:
                headA = headA.next
                y+=1
        print(headA.val, headB.val)
        
        a = headA
        b = headB
        while a is not None:
            if a==b:
                return a
            b = b.next
            a = a.next
        return None

        