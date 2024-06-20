# 使用者：姜海波
# 创建时间：2023/6/8  22:34
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(1000000)
        ans = take = 0
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                take += 1
                ans -= nums[i]
            else:
                give = min(take, nums[i] - nums[i - 1] - 1)
                ans += give * (give + 1) // 2 + give * nums[i - 1]
                take -= give

        return ans
