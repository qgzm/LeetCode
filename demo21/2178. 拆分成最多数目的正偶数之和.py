# 使用者：姜海波
# 创建时间：2023/5/8  16:46
from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        res = [2]
        finalSum -= 2
        while res[-1] < finalSum:
            finalSum -= res[-2] + 2
            res.append(res[-1] + 2)
        res[-1] += finalSum
        return res
