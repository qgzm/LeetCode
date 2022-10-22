# 使用者：姜海波
# 创建时间：2022/10/22  16:25
from bisect import bisect_right
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n =len(startTime)
        jbos= sorted(zip(startTime,endTime,profit),key=lambda p:p[1])
        dp = [0]*(n+1)
        for i in range(1,n+1):
            # hi=i表示二分上界为i(默认为n)
            k=bisect_right(jbos,jbos[i-1][0],hi=i,key=lambda p:p[1])
            dp[i]=max(dp[i-1],dp[k]+jbos[i-1][2])
        return dp[n]
