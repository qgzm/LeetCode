# 使用者：姜海波
# 创建时间：2023/3/17  9:16
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot + 1
        return nums[low]
