# 使用者：姜海波
# 创建时间：2023/3/29  15:22
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        canGet = 0
        ans = 0
        i = 0
        while canGet < n:
            if i < len(nums) and nums[i] <= canGet + 1:
                canGet += nums[i]
                i += 1
            else:
                canGet += canGet + 1
                ans += 1

        return ans
