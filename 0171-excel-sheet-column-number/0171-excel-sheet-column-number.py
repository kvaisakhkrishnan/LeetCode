class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count = 0
        for i in columnTitle:
            count *= 26
            count+=(ord(i)-64)
        return count