# 使用者：姜海波
# 创建时间：2022/10/16  18:21
from collections import deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 深度优先搜索
        # g = [[] for _ in range(n)]
        # for x, y in dislikes:
        #     g[x - 1].append(y - 1)
        #     g[y - 1].append(x - 1)
        # color = [0] * n
        #
        # # color[x]=0表示未访问结点x
        # def dfs(x, c) -> bool:
        #     color[x] = c
        #     return all(color[y] != c and (color[y] or dfs(y, -c)) for y in g[x])
        #
        # return all(c or dfs(i, 1) for i, c in enumerate(color))
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        color = [0] * n  # color[x] = 0 表示未访问节点 x
        for i, c in enumerate(color):
            if c == 0:
                q = deque([i])
                color[i] = 1
                while q:
                    x = q.popleft()
                    for y in g[x]:
                        if color[y] == color[x]:
                            return False
                        if color[y] == 0:
                            color[y] = -color[x]
                            q.append(y)
        return True



Solution().possibleBipartition(4,[[1, 2], [1, 3], [2, 4]])
