# 使用者：姜海波
# 创建时间：2023/1/24  0:26
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)

        for i, (cx, cy, cr) in enumerate(queries):
            for (px, py) in points:
                if (cx - px) ** 2 + (cy - py) ** 2 <= cr ** 2:
                    ans[i] += 1

        return ans

