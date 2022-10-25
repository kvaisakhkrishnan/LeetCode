class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = len(s)
        i//=2
        x=0
        y = len(s)-1
        while x < i:
            s[x],s[y-x] = s[y-x],s[x]
            x+=1