# 使用者：姜海波
# 创建时间：2023/3/31  16:05
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]<=0:
                nums[i]=n+1
        for i in range(n):
            num=abs(nums[i])
            if num<=n:
                nums[num-1]=-abs(nums[num-1])
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1

