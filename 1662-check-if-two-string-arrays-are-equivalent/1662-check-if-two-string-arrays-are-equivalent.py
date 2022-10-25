class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if word1 == [] and word2 == []:
            return True
        i = 1
        while i < len(word1):
            word1[0] +=word1[i]
            i+=1
        j = 1
        while j < len(word2):
            word2[0] += word2[j]
            j+=1
        return word1[0] == word2[0]
        