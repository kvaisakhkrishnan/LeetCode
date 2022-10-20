# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        level = 1
        x = [root]
        y = []
        while(x or y):
            elem = x.pop()
            if(elem.left):
                y.append(elem.left)
            if elem.right:
                y.append(elem.right)
            if elem.left is None and elem.right is None:
                return level
            if(len(x)==0):
                x = y
                y = []
                level+=1
                
        