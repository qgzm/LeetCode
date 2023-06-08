# 使用者：姜海波
# 创建时间：2023/6/6  22:59
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        a=[]
        b=[]
        for i in grid:
            a.append(i)
        for i in zip(*grid):
            b.append(list(i))
        ans = 0
        for i in a:
            for j in b:
                if i==j:
                    ans+=1
        return ans
Solution().equalPairs([[3,1,2,2],
                       [1,4,4,4],
                       [2,4,2,2],
                       [2,5,2,2]])