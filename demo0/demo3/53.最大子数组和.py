# 使用者：姜海波
# 创建时间：2022/9/5  15:38
from typing import List
from cmath import inf


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # # 贪心算法
        # n = len(nums)
        # for i in range(1, n):
        #     if nums[i - 1] > 0:
        #         nums[i] += nums[i - 1]
        #
        # return max(nums)

        # 动态规划
        if not nums:
            return -inf
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(cur_sum, max_sum)
        return max_sum
