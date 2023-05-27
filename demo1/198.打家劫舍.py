# 使用者：姜海波
# 创建时间：2023/5/23  14:22
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        le = len(nums)
        if le == 1:
            return nums[0]
        dp = [0] * le
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, le):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[- 1]
