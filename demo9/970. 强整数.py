# 使用者：姜海波
# 创建时间：2023/5/2  22:39
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        value1 = 1
        for i in range(21):
            value2 = 1
            for j in range(21):
                value = value1 + value2
                if value <= bound:
                    res.add(value)
                else:
                    break
                value2 *= y
            if value1 > bound:
                break
            value1 *= x
        return list(res)