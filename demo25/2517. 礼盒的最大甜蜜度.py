# 使用者：姜海波
# 创建时间：2023/6/1  2:02
from cmath import inf
from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def check( price: List[int], k: int, tastiness: int) -> bool:
            prev = -inf
            cnt = 0
            for p in price:
                if p - prev >= tastiness:
                    cnt += 1
                    prev = p
            return cnt >= k

        price.sort()
        left, right = 0, price[-1] - price[0]
        while left < right:
            mid = (left + right + 1) // 2
            if check(price, k, mid):
                left = mid
            else:
                right = mid - 1
        return left
