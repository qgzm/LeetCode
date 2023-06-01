# 使用者：姜海波
# 创建时间：2023/5/30  14:07
from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        j = 0
        i = 0
        while i < len(nums):
            if nums[i:i + len(groups[j])] == groups[j]:
                j += 1
                if j == len(groups):
                    return True
                i += len(groups[j-1])
            else:
                i += 1

        return False


print(Solution().canChoose([[1, 2, 3], [3, 4]], [7, 7, 1, 2, 3, 4, 7, 7]))