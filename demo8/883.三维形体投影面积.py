# 使用者：姜海波
# 创建时间：2023/3/26  17:26
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    ans+=1
        for a in grid:
            ans+=max(a)
        for i in range(n):
            ad=0
            for j in range(m):
                ad=max(ad,grid[j][i])
            ans+=ad

        return ans

