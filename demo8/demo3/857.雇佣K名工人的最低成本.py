# 使用者：姜海波
# 创建时间：2022/9/11  15:02
from cmath import inf
from heapq import heappush, heappop
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = sorted(zip(quality, wage), key=lambda p: p[1] / p[0])
        ans = inf
        totalq = 0
        h = []
        for q, w in pairs[:k - 1]:
            totalq += q
            heappush(h, -q)
        for q, w in pairs[k - 1:]:
            totalq += q
            heappush(h, -q)
            ans = min(ans, w / q * totalq)
            totalq += heappop(h)
        return ans
m=[10,20,5]
n=[70,50,30]

l=2
Solution().mincostToHireWorkers(m,n,l)
