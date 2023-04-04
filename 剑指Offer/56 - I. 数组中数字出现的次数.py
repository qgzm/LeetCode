# 使用者：姜海波
# 创建时间：2023/4/4  22:31
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        index = 0
        n = 0
        for i in nums:
            n ^= i

        while n & 1 == 0:
            index += 1
            n >>= 1
        r1, r2 = 0, 0
        for j in nums:
            if (j >> index) & 1 == 0:
                r1 ^= j
            else:
                r2 ^= j
        return [r1, r2]
