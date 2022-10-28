class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash = [0]*26
        for i in s:
            pos = ord(i)-ord('a')
            hash[pos]+=1
        for j in t:
            pos = ord(j)-ord('a')
            hash[pos]-=1
        i = 0
        while i < 26:
            if hash[i] < 0 or hash[i]>0:
                return chr(i+ord('a'))
                
            i+=1
        