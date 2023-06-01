# 使用者：姜海波
# 创建时间：2023/6/1  12:46
from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a = sum(aliceSizes)
        b = sum(bobSizes)
        diff = (a - b) // 2
        hab=set(bobSizes)
        for i in aliceSizes:
            if i - diff in hab:
                return [i, i - diff]
