# 使用者：姜海波
# 创建时间：2023/5/21  15:46
from typing import List


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        n = len(bucket)
        maxk = max(vat)
        if maxk == 0:
            return 0
        res = float('inf')
        for k in range(1, maxk + 1):
            t = 0
            for i in range(n):
                t += max(0, (vat[i] + k - 1) // k - bucket[i])
            res = min(res, t + k)
        return res
