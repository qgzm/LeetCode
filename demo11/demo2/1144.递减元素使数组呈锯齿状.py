# 使用者：姜海波
# 创建时间：2023/2/27  23:18
from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def help(pos: int):
            res = 0
            for i in range(pos, len(nums), 2):
                a = 0
                if i - 1 >= 0:
                    a = max(a, nums[i] - nums[i - 1] + 1)
                if i + 1 < len(nums):
                    a = max(a, nums[i] - nums[i + 1] + 1)
                res += a
            return res

        return min(help(0), help(1))
