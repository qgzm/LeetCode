# 使用者：姜海波
# 创建时间：2023/6/7  22:52
import heapq
from typing import List
import b

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)
        for i in range(n):
            piles[i] = -piles[i]
        heapq.heapify(piles)
        for i in range(k):
            tmp = heapq.heappop(piles)
            heapq.heappush(piles, tmp + (-tmp) // 2)
        return -sum(piles)
