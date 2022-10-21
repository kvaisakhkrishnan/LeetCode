class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        x = x[len(x)-1]
        return len(x)