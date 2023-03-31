# 使用者：姜海波
# 创建时间：2023/3/31  9:09
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            # need为需要运送的天数
            # cur为当前这一天已经运送的包裹重量之和
            need, cur = 1, 0
            for weight in weights:
                if cur + weight > mid:
                    need += 1
                    cur = 0
                cur += weight
            if need <= days:
                right = mid
            else:
                left = mid + 1
        return left
