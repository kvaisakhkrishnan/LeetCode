# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        self.invert(root)
        return root
    
    def invert(self, a):
        if a is None:
            return
        a.left, a.right = a.right, a.left
        self.invert(a.left)
        self.invert(a.right)