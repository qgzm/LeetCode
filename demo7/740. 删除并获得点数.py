# 使用者：姜海波
# 创建时间：2023/4/29  23:12
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ma = max(nums)
        dp = [0] * (ma + 1)
        for i in nums:
            dp[i] += i
        for i in range(2, ma + 1):
            dp[i] = max(dp[i - 2] + dp[i], dp[i - 1])
        return dp[-1]


print(Solution().deleteAndEarn([3, 4, 2]))
