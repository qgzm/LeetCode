# 使用者：姜海波
# 创建时间：2023/4/2  14:27
from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        integ = 0
        ans = []
        for i in nums:
            integ <<= 1
            integ += int(i)
            integ %= 10
            ans.append(integ % 5 == 0)

        return ans
