# 使用者：姜海波
# 创建时间：2023/4/29  22:26
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
