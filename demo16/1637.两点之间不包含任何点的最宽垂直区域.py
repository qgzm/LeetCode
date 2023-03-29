# 使用者：姜海波
# 创建时间：2023/3/29  14:13
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        lis=[]
        for i in range(1,len(points)):
            lis.append(points[i][0]-points[i-1][0])
        return max(lis)


print(Solution().maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))