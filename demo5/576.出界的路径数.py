# 使用者：姜海波
# 创建时间：2023/3/24  13:50
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # 动态规划
        # dp[i][j][k] = dp[i-1][j][k-1] + dp[i+1][j][k-1] + dp[i][j-1][k-1] + dp[i][j+1][k-1]
        MOD = 10 ** 9 + 7
        outCount = 0
        dp = [[[0] * n for i in range(m)] for j in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1
        for i in range(maxMove):
            for j in range(m):
                for k in range(n):
                    if dp[i][j][k] > 0:
                        for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                            if 0 <= j1 < m and 0 <= k1 < n:
                                dp[i + 1][j1][k1] = (dp[i + 1][j1][k1] + dp[i][j][k]) % MOD
                            else:
                                outCount = (outCount + dp[i][j][k]) % MOD

        return outCount
