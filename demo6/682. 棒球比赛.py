# 使用者：姜海波
# 创建时间：2023/4/7  10:11
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = 0
        points = []
        for op in operations:
            if op == '+':
                pt = points[-1] + points[-2]
            elif op == 'D':
                pt = points[-1] * 2
            elif op == 'C':
                ans -= points.pop()
                continue
            else:
                pt = int(op)
            ans += pt
            points.append(pt)
        return ans
