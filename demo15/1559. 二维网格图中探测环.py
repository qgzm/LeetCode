# 使用者：姜海波
# 创建时间：2023/6/8  17:22
import collections
from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        path = set()

        # p->不能回头
        def dfs(node, p):
            if node in path:
                return True
            path.add(node)
            i, j = node
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) != p and grid[x][y] == grid[i][j]:
                    if dfs((x, y), node):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if (i, j) not in path and dfs((i, j), None):
                    return True
        return False


print(Solution().containsCycle(
    grid=[["a", "a", "a", "a"],
          ["a", "b", "b", "a"],
          ["a", "b", "b", "a"],
          ["a", "a", "a", "a"]]))
