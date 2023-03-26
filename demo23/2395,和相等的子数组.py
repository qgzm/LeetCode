# 使用者：姜海波
# 创建时间：2023/3/26  15:00
from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        arr = []
        for i in range(1, len(nums)):
            arr.append(nums[i - 1] + nums[i])

        if len(set(arr)) < len(arr):
            return True
        else:
            return False
