class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mat =[[0 for i in range(amount + 1)] for i in range(len(coins))]
        for i in range(len(coins)):
            for j in range(amount+1):
                if(i == 0):
                    if(j % coins[i] == 0):
                        mat[i][j] = 1
                else:
                    if(j < coins[i]):
                        mat[i][j] = mat[i-1][j]
                    else:
                        diff = j - coins[i]
                        val = mat[i][diff]
                        mat[i][j] = mat[i-1][j] + val
        print(mat)
        return mat[len(coins)-1][amount]