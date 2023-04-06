# 使用者：姜海波
# 创建时间：2023/4/6  10:06
import collections
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        edge = collections.defaultdict(list)
        for i, (x1, y1) in enumerate(stones):
            for j, (x2, y2) in enumerate(stones):
                if x1 == x2 or y1 == y2:
                    edge[i].append(j)

        def dfs(x: int):
            vis.add(x)
            for y in edge[x]:
                if y not in vis:
                    dfs(y)

        vis = set()
        num = 0
        for i in range(n):
            if i not in vis:
                num += 1
                dfs(i)

        return n - num



        # dict_x = collections.defaultdict(list)
        # dict_y = collections.defaultdict(list)
        # # 将坐标存入字典
        # for x, y in stones:
        #     dict_x[x].append((x, y))
        #     dict_y[y].append((x, y))
        # visited = set()
        #
        # def dfs(node:tuple):
        #     if node in visited:
        #         return
        #     visited.add(node)
        #     x, y = node
        #     for i in dict_x[x]:
        #         dfs(i)
        #     for i in dict_y[y]:
        #         dfs(i)
        #
        # ans = 0
        # for i in stones:
        #     i = tuple(i)
        #     if i not in visited:
        #         ans += 1
        #         dfs(i)
        # return len(stones) - ans


print(Solution().removeStones(stones=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))