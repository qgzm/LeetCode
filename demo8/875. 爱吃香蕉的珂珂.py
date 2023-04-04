# 使用者：姜海波
# 创建时间：2023/4/4  16:41
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(i:int)->bool:
            su=0
            for j in piles:
                su+=j//i+1
            return su>h



        left=1
        right=max(piles)+1
        while left<right:
            mid = left+(right-left)//2
            if check(mid):
                left=mid+1
            else:
                right=mid-1

        return left


print(Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 5))
