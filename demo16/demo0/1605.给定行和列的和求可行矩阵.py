# 使用者：姜海波
# 创建时间：2023/3/14  11:16
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        res = [[0] * m for _ in range(n)]
        i = j = 0
        while i < n and j < m:
            v = min(rowSum[i], colSum[j])
            res[i][j] = v
            rowSum[i] -= v
            colSum[j] -= v
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1

        return res
