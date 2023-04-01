# 使用者：姜海波
# 创建时间：2023/4/1  14:14
from collections import defaultdict
from itertools import pairwise

from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        d = defaultdict(list)

        for i in words:
            d[tuple(ord(x) - ord(y) for x, y in pairwise(i))].append(i)
        x, y = d.values()
        return x[0] if len(x) == 1 else y[0]


print(Solution().oddString(
    ["adc", "wzy", "abc"]))
