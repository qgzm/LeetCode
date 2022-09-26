# 使用者：姜海波
# 创建时间：2022/9/26  23:33
from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        l = len(nums) + 2
        sum_ = 0
        for x in nums:
            sum_ += x
        sumTwo = int(l * (l + 1) / 2) - sum_
        limit = sumTwo // 2
        sum_ = 0
        for x in nums:
            if x <= limit:
                sum_ += x
            one = int(limit * (limit + 1) // 2) - sum_
            one = int(one)
            two = (sumTwo - one).__int__()
        return [one, two]


print(Solution().missingTwo([1]))
