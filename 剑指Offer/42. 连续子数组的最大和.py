# 使用者：姜海波
# 创建时间：2023/4/21  22:38
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nur_sum = ans_sum = nums[0]
        for i in range(1, len(nums)):
            nur_sum = max(nums[i], nur_sum + nums[i])
            ans_sum = max(nur_sum, ans_sum)
        return ans_sum
