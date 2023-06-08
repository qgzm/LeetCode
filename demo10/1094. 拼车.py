# 使用者：姜海波
# 创建时间：2023/6/6  15:15
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l=max([a[2]for a in trips])

        # le=len(trips[0])
        arr=[0]*(l+1)
        for i,j,k in trips:
            arr[j]+=i
            arr[k]-=i
        ans=0
        ma=0
        for i in arr:
            ans+=i
            ma=max(ma,ans)
        return ma<=capacity
Solution().carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4)