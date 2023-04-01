# 使用者：姜海波
# 创建时间：2023/3/31  23:19
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        numset = set(nums)
        for i in nums:
            if i + diff in numset and i + diff * 2 in numset:
                ans += 1

        return ans
