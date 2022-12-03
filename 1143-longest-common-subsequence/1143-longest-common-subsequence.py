class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mat = [[0 for i in range(len(text1)+1)] for i in range (len(text2)+1)]
        print(mat)
        for i in range(len(text2)):
            for j in range(len(text1)):
                x = i+1
                y = j+1
                if(text2[i] == text1[j]):
                    mat[x][y] = 1 + mat[x-1][y-1]
                else:
                    mat[x][y] = max(mat[x-1][y], mat[x][y-1])
        return mat[len(text2)][len(text1)]
        