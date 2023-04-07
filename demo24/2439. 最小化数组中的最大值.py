# 使用者：姜海波
# 创建时间：2023/4/6  22:13
from math import ceil
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        sum = 0
        for i, j in enumerate(nums):
            sum += j
            ans = max(ans, ceil(sum / (i + 1)))

        return ans
