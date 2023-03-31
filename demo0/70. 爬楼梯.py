# 使用者：姜海波
# 创建时间：2023/3/31  17:24
class Solution:
    def numWays(self, n: int) -> int:
        # if n==1 or n==0:
        #     return 1
        #
        # dp = [0] * (n+1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, n+1):
        #     dp[i] = dp[i - 2] + dp[i - 1]
        # return dp[n]%(10**9+7)
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a