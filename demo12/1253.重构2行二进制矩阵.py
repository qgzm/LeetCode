# 使用者：姜海波
# 创建时间：2023/4/6  20:25
from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        k = sum(x == 2 for x in colsum)
        upper, lower = upper - k, lower - k
        if upper < 0 or lower < 0:
            return []
        n = len(colsum)
        matrix = [[0] * n for _ in range(2)]
        for i in range(n):
            if colsum[i] == 2:
                matrix[0][i] = matrix[1][i] = 1
            elif colsum[i] == 1:
                if upper > 0:
                    matrix[0][i] = 1
                    upper -= 1
                else:
                    matrix[1][i] = 1
        return matrix
