# @Time : 2024/8/4 18:55
# @Author : 姜海波
# @Version：V 0.1
# @File : 3143. 正方形中的最多点数.py
# @desc :
from cmath import inf
from typing import List


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        min1 = [inf] * 26
        min2 = inf
        n = len(s)
        for i in range(n):
            x, y = points[i]
            j = ord(s[i]) - ord('a')
            d = max(abs(x), abs(y))
            if d < min1[j]:
                min2 = min(min2, min1[j])
                min1[j] = d
            elif d < min2:
                min2 = d

        return sum(d < min2 for d in min1)
