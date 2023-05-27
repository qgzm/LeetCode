# 使用者：姜海波
# 创建时间：2023/5/26  10:57
from cmath import inf
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> float | list[float]:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        dist = [[inf] * n for _ in range(n)]
        dist[0][0] = 1
        queue = deque([(0, 0)])
        while queue:
            x, y = queue.popleft()
            if x == y == n - 1:
                return dist[x][y]
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n:
                        continue
                    if grid[x + dx][y + dy] == 1 or dist[x + dx][y + dy] <= dist[x][y] + 1:
                        continue
                    dist[x + dx][y + dy] = dist[x][y] + 1
                    queue.append((x + dx, y + dy))
        return -1
