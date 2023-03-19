# 使用者：姜海波
# 创建时间：2023/3/19  17:35
from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        lis = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2,1]]
        def dfs(x,y,z):
            if grid[x][y]==n*n-1:
                return True

            for i in lis:
                mm=i[0]+x
                nn=i[1]+y
                if mm<0 or nn<0 or mm>=n or nn>=n:
                    continue
                if grid[mm][nn]==z:
                    return dfs(mm,nn,z+1)


            return False

        if grid[0][0] != 0:
            return False
        return dfs(x,y,z)


print(Solution().checkValidGrid([
    [24,11,22,17,4],
    [21,16,5,12,9],
    [6,23,10,3,18],
    [15,20,1,8,13],
    [0,7,14,19,2]]))