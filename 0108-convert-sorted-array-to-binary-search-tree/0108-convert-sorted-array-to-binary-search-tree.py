# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return
        root = TreeNode()
        x = len(nums)
        x = x//2
        root.val = nums[x]
        print(root.val)
        if x!=0:
            root.left = TreeNode()
            self.buildTree(nums[0:x],root.left)
        if x!=len(nums)-1:
            root.right = TreeNode()
            self.buildTree(nums[x+1:len(nums)],root.right)
        return root
    
    def buildTree(self,nums, x):
        #print(nums)
        y = len(nums)
        y = y//2
        x.val = nums[y]
        print(x.val)
        if y!=0:
            x.left = TreeNode()
            self.buildTree(nums[0:y],x.left)
        if y!=len(nums)-1:
            x.right = TreeNode()
            self.buildTree(nums[y+1:len(nums)],x.right)