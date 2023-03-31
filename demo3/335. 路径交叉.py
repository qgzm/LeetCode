# 使用者：姜海波
# 创建时间：2023/3/30  16:18
from typing import List


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        i = 0
        # 第一种情况,对于每一次移动i,第i次移动距离都比第i-2次移动距离更长
        # 短路,牛
        while i < n and (i < 2 or distance[i] > distance[i - 2]):
            i += 1
        # 对于每一次移动i<j,都满足第一种情况,对于每一次移动i>j,都满足第二种情况
        if i == n:
            return False
        if ((i == 3 and distance[i] >= distance[i - 2]) or
                (i >= 4 and distance[i] >= distance[i - 2] - distance[i - 4])):
            distance[i - 1] -= distance[i - 3]
        i += 1
        # 第二种情况,对于每次移动i,第i次移动距离都比第都i-2次移动距离都更短
        while i < n and distance[i] < distance[i - 2]:
            i += 1

        return i != n
