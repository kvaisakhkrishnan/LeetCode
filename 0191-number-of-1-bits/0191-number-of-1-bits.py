class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            val = n%2
            if val == 1:
                count+=1
            n//=2
        return count
        