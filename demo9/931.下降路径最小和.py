# 使用者：姜海波
# 创建时间：2023/3/28  13:09
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        for i in range(1, m):
            # min(row[max(0,i-1): min(len(row), i+2)])
            for j in range(m):
                if j == 0:
                    matrix[i][j] += min(matrix[i - 1][0], matrix[i - 1][1])
                elif j == m - 1:
                    matrix[i][j] += min(matrix[i - 1][m - 2], matrix[i - 1][m - 1])
                else:
                    matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j],matrix[i-1][j+1])

        return min(matrix[m-1])
