# 使用者：姜海波
# 创建时间：2023/5/7  21:42
import collections
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cou = [0] * 60
        for i in time:
            cou[i % 60] += 1
        res = 0
        for i in range(1, 30):
            res += cou[i] * cou[60 - i]
        res += cou[0] * (cou[0] - 1) // 2 + cou[30] * (cou[30] - 1) // 2
        return res
