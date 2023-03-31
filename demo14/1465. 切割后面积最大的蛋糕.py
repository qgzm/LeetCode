# 使用者：姜海波
# 创建时间：2023/3/31  14:28
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hor=0
        ver=0
        horizontalCuts=[0]+horizontalCuts+[h]
        horizontalCuts.sort()
        verticalCuts=[0]+verticalCuts+[w]
        verticalCuts.sort()
        for i in range(1,len(horizontalCuts)):
            hor=max(horizontalCuts[i]-horizontalCuts[i-1],hor)
        for i in range(1,len(verticalCuts)):
            ver=max(verticalCuts[i]-verticalCuts[i-1],ver)

        return hor*ver%(10**9+7)
