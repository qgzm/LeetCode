# 使用者：姜海波
# 创建时间：2022/12/19  22:45
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 并查集
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        p = list(range(n))
        # 合并并查集
        for u, v in edges:
            p[find(u)] = find(v)
        return find(source) == find(destination)


Solution().validPath(3,
                     [[0, 1], [1, 2], [2, 0]],
                     0,
                     2)
