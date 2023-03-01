# 使用者：姜海波
# 创建时间：2023/3/1  12:36
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        class Solution:
            def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
                n = len(grid)
                ans = [[0] * (n - 2) for _ in range(n - 2)]
                for i in range(n - 2):
                    for j in range(n - 2):
                        ans[i][j] = max(grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3))
                return ans

