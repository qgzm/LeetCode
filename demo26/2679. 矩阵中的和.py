# 使用者：姜海波
# 创建时间：2023/6/3  17:45
from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        return sum(map(max,zip(*nums)))

# ma=[[1,2],[3,4],[5,6]]
# for i in zip(*ma):
#     print(i)