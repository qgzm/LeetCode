# 使用者：姜海波
# 创建时间：2023/4/4  16:24
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(i: int) -> bool:
            res = 0
            for c in candies:
                res += c // i
            return res >= k

        l = 1
        r = max(candies) + 1
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1
