# 使用者：姜海波
# 创建时间：2023/5/4  22:22
from cmath import inf
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[inf]*(len(nums))
        dp[0]=0
        for index,i in enumerate(nums):
            for j in range(index+1,index+i+1):
                if j<len(nums):
                    dp[j]=min(dp[j],dp[index]+1)
                else:
                    return int(dp[-1])
        return dp[-1]

print(Solution().jump([0]))