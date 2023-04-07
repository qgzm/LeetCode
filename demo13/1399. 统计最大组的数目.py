# 使用者：姜海波
# 创建时间：2023/4/7  13:21
class Solution:
    def countLargestGroup(self, n: int) -> int:
        ans = [0] * 37
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i // 10] + i % 10
            ans[dp[i]] += 1
        ma = max(ans)
        return sum(i == ma for i in ans)
