# 使用者：姜海波
# 创建时间：2023/6/8  21:29
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[0]*(days[-1]+1)
        day=set(days)
        for i in range(1,days[-1]+1):
            if i not in day:
                dp[i]=dp[i-1]
            else:
                dp[i]=min(dp[max(0,i-1)]+costs[0],dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2])
        return dp[-1]


print(Solution().mincostTickets([1, 4, 6, 7, 8, 20], [7, 2, 15]))