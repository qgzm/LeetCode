# 使用者：姜海波
# 创建时间：2023/1/26  11:40
from typing import List


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        print(nums)


Solution().minOperations([2, 3, 2, 4, 3], [9, 6, 9, 3, 15])
