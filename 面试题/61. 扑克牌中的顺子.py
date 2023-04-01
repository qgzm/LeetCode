# 使用者：姜海波
# 创建时间：2023/4/1  23:22
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat=set()
        ma,mi=0,14
        for i in nums:
            if i==0:
                continue
            ma=max(ma,i)
            mi=min(mi,i)
            if i in repeat:
                return False
            repeat.add(i)
        return ma-mi<5


