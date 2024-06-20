from typing import List  # 使用者：姜海波
# 创建时间：2023/6/8  16:07
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        top=sum(grid[0][1:])
        bottom=0
        ans=max(bottom,top)
        for i in range(1,n):
            top-=grid[0][i]
            bottom+=grid[1][i-1]
            ans=min(ans,max(bottom,top))

        return ans