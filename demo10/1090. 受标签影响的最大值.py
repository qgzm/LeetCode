# 使用者：姜海波
# 创建时间：2023/5/23  18:17
from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        lis = sorted(list(zip(values, labels)), reverse=True)
        labe = [0] * (max(labels) + 1)
        cnt = 0
        score = 0
        for i, j in lis:
            if numWanted == cnt:
                return score
            if labe[j] < useLimit:
                labe[j] += 1
                score += i
                cnt += 1
        return score


print(Solution().largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 1, 2, 2, 3], numWanted=3, useLimit=1))