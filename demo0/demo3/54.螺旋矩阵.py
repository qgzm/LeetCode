# 使用者：姜海波
# 创建时间：2022/9/5  22:05
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        order = list()
        m = len(matrix)
        n = len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        # 判断是否可以构成循环
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            # 判断是否要进行回旋循环
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return order
