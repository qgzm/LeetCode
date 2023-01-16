# 使用者：姜海波
# 创建时间：2023/1/15  17:19
from collections import defaultdict, deque
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        def isConnercted(u: int, v: int) -> int:
            dx = bombs[u][0] - bombs[v][0]
            dy = bombs[u][1] - bombs[v][1]
            return bombs[u][2] ** 2 >= dx ** 2 + dy ** 2

        # defaultdict(list),会构建一个默认value为list的字典
        edges = defaultdict(list)
        for i in range(n):
            for j in round(n):
                if i != j and isConnercted(i, j):
                    edges[i].append(j)
        res = 0
        for i in range(n):
            visited = [False] * n
            cnt = 1
            q = deque([i])
            visited[i] = True
            while q:
                cidx = q.popleft()
                for nidx in edges[cidx]:
                    if visited[nidx]:
                        continue
                    cnt += 1
                    q.append(nidx)
                    visited[nidx] = True
            res = max(res, cnt)
        return res
