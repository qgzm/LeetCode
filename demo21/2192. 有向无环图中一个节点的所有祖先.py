# @Time : 2024/8/4 22:01
# @Author : 姜海波
# @Version：V 0.1
# @File : 2192. 有向无环图中一个节点的所有祖先.py
# @desc :
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[y].append(x)  # 反向建图

        def dfs(x: int) -> None:
            vis[x] = True  # 避免重复访问
            for y in g[x]:
                if not vis[y]:
                    dfs(y)  # 只递归没有访问过的点

        ans = [None] * n
        for i in range(n):
            vis = [False] * n
            dfs(i)  # 从 i 开始 DFS
            vis[i] = False  # ans[i] 不含 i
            ans[i] = [j for j, b in enumerate(vis) if b]
        return ans

# a, b, c, d = [None] * 2, [] * 2, [[] * 2], [[] for _ in range(2)]
# # [None, None] [] [[]] [[], []]
# a[0]=[1]
# # b[0]=[1]
# c[0][0]=[1]
# d[0]=[1]
# print(a,b,c,d)
