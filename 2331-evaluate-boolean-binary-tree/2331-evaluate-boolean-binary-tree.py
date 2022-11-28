# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        self.postOrder(root)
        return root.val
    def postOrder(self, x):
        
        if not x or x.val == 1 or x.val == 0:
            return
        self.postOrder(x.left)
        self.postOrder(x.right)
        if x.val == 2:
            x.val = x.left.val or x.right.val
        else:
            x.val = x.left.val and x.right.val
        