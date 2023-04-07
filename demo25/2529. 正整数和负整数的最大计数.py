# 使用者：姜海波
# 创建时间：2023/4/6  22:20
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        less = great = 0
        for x in nums:
            if x < 0:
                less += 1
            elif x > 0:
                great += 1
        return max(less, great)



