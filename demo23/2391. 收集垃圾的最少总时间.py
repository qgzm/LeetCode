# 使用者：姜海波
# 创建时间：2023/5/31  2:03
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        right = {}
        for i, s in enumerate(garbage):
            ans += len(s)
            for c in s:
                right[c] = i
        return ans + sum(sum(travel[:r]) for r in right.values())

