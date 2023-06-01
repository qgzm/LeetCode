# 使用者：姜海波
# 创建时间：2023/5/30  14:54
from typing import List


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        row_mask = []
        for row in matrix:
            s = 0
            for j, k in enumerate(row):
                s += k << j
            row_mask.append(s)
        ans = 0
        for set in range(1 << len(matrix[0])):
            if set.bit_count() == numSelect:
                res = 0
                for row in row_mask:
                    if row & set == row:
                        res += 1
                ans = max(ans, res)
        return ans
