# 使用者：姜海波
# 创建时间：2023/3/30  15:49
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<3:
            return False
        first,second=nums[0],float('inf')
        for i in range(1,n):
            num=nums[i]
            if num>second:
                return True
            if num>first:
                second=num
            else:
                first=num

        return False
