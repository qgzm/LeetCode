# 使用者：姜海波
# 创建时间：2023/6/8  9:55
import queue
from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        que = deque([(entrance[0], entrance[1], 0)])
        x = [1, 0, -1, 0]
        y = [0, -1, 0, 1]
        maze[entrance[0]][entrance[1]] = '+'
        while que:
            a, b, d = que.popleft()
            for i in range(4):
                ax = a + x[i]
                ay = b + y[i]
                if 0 <= ax < m and 0 <= ay < n and maze[ax][ay] == ".":
                    if ax == 0 or ay == 0 or ax == m - 1 or ay == n - 1:
                        return d + 1

                    maze[ax][ay] = '+'
                    que.append((ax, ay, d + 1))
        return -1


print(Solution().nearestExit([["+", "+", "+"],
                              [".", ".", "."],
                              ["+", "+", "+"]], [1, 0]))
