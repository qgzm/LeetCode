# 使用者：姜海波
# 创建时间：2023/4/12  22:59
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in set(nums):
            return 0
        ans = 0
        for i in nums:
            if i < 0:
                ans += 1
        return -1 if ans % 2 == 1 else 1
