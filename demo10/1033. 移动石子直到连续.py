# 使用者：姜海波
# 创建时间：2023/4/6  16:01
from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        sort_abc = sorted([a, b, c])
        a, b, c = sort_abc[0], sort_abc[1], sort_abc[2],
        # a,b,c位置已经连续
        if a + 1 == b and b + 1 == c:
            return [0, 0]
        return [1 if (b - a <= 2 or c - b <= 2) else 2, c - a - 2]

