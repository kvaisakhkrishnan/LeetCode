# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return
        queue = [root]
        sum = 0
        while len(queue):
            elem = queue.pop(0)
            if elem.left:
                queue.append(elem.left)
            if elem.right:
                queue.append(elem.right)
            if(elem.val>=low and elem.val<=high):
                sum += elem.val
        return sum
        