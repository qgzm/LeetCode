# 使用者：姜海波
# 创建时间：2023/4/2  14:46
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        su = 0
        for i in nums:
            su += i
            ans.append(su)

        return ans
