# 使用者：姜海波
# 创建时间：2023/3/26  15:10
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(cards)==len(set(cards)):
            return -1
        dct,ans={},len(cards)+1
        for i ,card in enumerate(cards):
            if card in dct:
                ans=min(ans,i-dct[card]+1)
            dct[card]=i
        return ans
