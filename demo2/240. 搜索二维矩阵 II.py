# 使用者：姜海波
# 创建时间：2023/3/31  19:22
import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for row in matrix:
        #     idx = bisect.bisect_left(row, target)
        #     if idx < len(row) and row[idx] == target:
        #         return True
        # return False
        m,n=len(matrix),len(matrix[0])
        x,y=0,n-1
        while x<m and y>=0:
            if matrix[x][y]==target:
                return True
            if matrix[x][y]>target:
                y-=1
            else:
                x+=1
        return False
