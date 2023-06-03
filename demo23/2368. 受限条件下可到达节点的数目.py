# 使用者：姜海波
# 创建时间：2023/6/3  17:03
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        r = set(restricted)
        g = [[] for _ in range(n)]
        for x, y in edges:
            if x not in r and y not in r:
                g[x].append(y)
                g[y].append(x)
        ans = 0

        def dfs(x: int, fa: int) -> None:
            nonlocal ans
            ans += 1
            for y in g[x]:
                if y!=fa:
                    dfs(y,x)
        dfs(0,-1)
        return ans
