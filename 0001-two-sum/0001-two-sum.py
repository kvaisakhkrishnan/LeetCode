class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        k = 0
        while k<len(nums):
            
            i = nums[k]
            j = target-i
            if j in nums:
                if k == nums.index(j):
                    pass
                else:
                    pos = [k, nums.index(j)]
                    return pos
            k+=1
                
        