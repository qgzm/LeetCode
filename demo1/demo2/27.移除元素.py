# 使用者：姜海波
# 创建时间：2022/9/3  16:30
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        k = 0
        n = len(nums)
        while j < n:
            if nums[j] != val:
                nums[k] = nums[j]
                k += 1
            j += 1
        return k