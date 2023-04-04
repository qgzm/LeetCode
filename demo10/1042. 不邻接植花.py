# 使用者：姜海波
# 创建时间：2023/4/4  20:22
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        res = [] * n
        G = [[] for _ in range(n)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(n):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()

        return res
