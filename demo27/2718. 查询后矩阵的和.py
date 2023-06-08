# 使用者：姜海波
# 创建时间：2023/6/6  15:24
from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        ans = 0
        vis = [set(), set()]
        for i, j, k in reversed(queries):
            if j not in vis[i]:
                ans += (n - len(vis[i ^ 1])) * k
                vis[i].add(j)
        return ans
