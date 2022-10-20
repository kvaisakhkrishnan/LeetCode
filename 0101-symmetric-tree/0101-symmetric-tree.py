# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.checkSymmetry(root.left, root.right)
        
    def checkSymmetry(self, x, y):
        if x is None and y is None:
            return True
        elif x is None or y is None:
            return False
        else:
            if x.val == y.val:
                return self.checkSymmetry(x.left, y.right) and self.checkSymmetry(x.right, y.left)
            
            
            
            