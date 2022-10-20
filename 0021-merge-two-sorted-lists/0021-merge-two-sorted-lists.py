# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a = list1
        b = list2
        if a is None and b is None:
            return
        if a is None:
            return b
        if b is None:
            return a
        head = ListNode()
        elem = head
        while a is not None and b is not None:
            if a.val < b.val:
                elem.val = a.val
                
                a = a.next
            else:
                elem.val = b.val
                b = b.next
            if a is not None and b is not None:
                elem.next = ListNode()
                elem = elem.next
        if a is not None:
            elem.next = a
        if b is not None:
            elem.next = b
        return head
            
        