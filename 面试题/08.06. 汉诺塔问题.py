# 使用者：姜海波
# 创建时间：2023/6/8  21:55
from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        self.move(self, n, A, B, C)

    def move(self, n, A, B, C):
        if n == 1:
            C.append(A[-1])
            A.pop()
            return
        else:
            self.move(n - 1, A, C, B)
            C.append(A[-1])
            A.pop()
            self.move(n - 1, B, A, C)
