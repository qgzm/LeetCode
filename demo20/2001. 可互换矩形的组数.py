# 使用者：姜海波
# 创建时间：2023/6/9  18:38
import collections
import math
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        res = 0
        dic = collections.defaultdict(int)
        for a, b in rectangles:
            x = math.gcd(a, b)
            a //= x
            b //= x
            dic[(a, b)] += 1
            res += dic[(a, b)] - 1
        return res
