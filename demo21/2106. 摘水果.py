# 使用者：姜海波
# 创建时间：2023/5/4  20:41
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # 要么一直向前走,要么先往一个方向移动x步,再向另个方向移动k-2x步
        # 或者当x处于0时,一直向一个方向移动
        left = 0
        right = 0
        n = len(fruits)
        sum = 0
        ans = 0

        def step(left: int, right: int) -> int:
            if fruits[right][0] <= startPos:
                return startPos - fruits[left][0]
            elif fruits[left][0] >= startPos:
                return fruits[right][0] - startPos
            else:
                return min(abs(startPos - fruits[right][0]), abs(startPos - fruits[left][0])) + fruits[right][0] - \
                       fruits[left][0]
        # 双指针
        while right < n:
            sum += fruits[right][1]
            while left <= right and step(left, right) > k:
                sum -= fruits[left][1]
                left += 1
            ans = max(ans, sum)
            right += 1
        return ans
