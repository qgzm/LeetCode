# 使用者：姜海波
# 创建时间：2023/6/8  23:14
import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # a = bisect.bisect_left(nums, target)
        # if nums[a] != target:
        #     return -1
        # else:
        #     return a
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
