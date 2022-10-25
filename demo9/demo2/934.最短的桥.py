# 使用者：姜海波
# 创建时间：2022/10/25  19:03
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v != 1:
                    continue
                q = []

                def dfs(x: int, y: int) -> None:
                    grid[x][y] = -1
                    q.append((x, y))
                    for nx, ny in (x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1):
                        # 防止越界
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            dfs(nx, ny)

                dfs(i, j)
                # 此时已经将第一个岛的所有值改为-1，即岛1“沉没”了，广度优先遍历所得的第一个1就是第二个岛
                step = 0
                while True:
                    tmq = q
                    q = []
                    for x, y in tmq:
                        for nx, ny in (x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1):
                            if 0 <= nx < n and 0 <= ny < n:
                                if grid[nx][ny] == 1:
                                    return step
                                if grid[nx][ny] == 0:
                                    grid[nx][ny] = -1
                                    q.append((nx, ny))
                    step += 1
