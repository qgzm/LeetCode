# 使用者：姜海波
# 创建时间：2023/4/4  13:14
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):

            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        le = len(dp)
        dp1 = []
        nums.reverse()
        for i in range(len(nums)):

            dp1.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp1[i] = max(dp1[j] + 1, dp1[i])
        dp1.reverse()
        ans = le
        for i in range(1, le - 1):  # 要求是山脉数组，所以需要两遍的递增子序列长度至少为2
            if dp[i] >= 2 and dp1[i] >= 2:
                ans = min(ans, le - (dp[i] + dp1[i] - 1))  # 下标重复计算，需要减一
        return ans


print(Solution().minimumMountainRemovals([9, 8, 1, 7, 6, 5, 4, 3, 2, 1]))
