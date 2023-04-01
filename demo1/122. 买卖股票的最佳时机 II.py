# 使用者：姜海波
# 创建时间：2023/4/1  14:48
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=[]
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1]>0:
                ans.append(prices[i]-prices[i-1])

        return sum(ans)
