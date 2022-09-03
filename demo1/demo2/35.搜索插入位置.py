# 使用者：姜海波
# 创建时间：2022/9/3  16:40
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
        if target >nums[i]:
            return i+1
        return i
