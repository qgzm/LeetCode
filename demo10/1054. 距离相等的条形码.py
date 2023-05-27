# 使用者：姜海波
# 创建时间：2023/5/14  13:38
import heapq
from collections import Counter
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # count = Counter(barcodes)
        # q = []
        # for x, cx in count.items():
        #     heapq.heappush(q, (-cx, x))
        # res = []
        # while len(q) > 0:
        #     cx, x = heapq.heappop(q)
        #     if len(res) == 0 or res[-1] != x:
        #         res.append(x)
        #         if cx < -1:
        #             heapq.heappush(q, (cx + 1, x))
        #     else:
        #         cy, y = heapq.heappop(q)
        #         res.append(y)
        #         if cy < -1:
        #             heapq.heappush(q, (cy + 1, y))
        #         heapq.heappush(q, (cx, x))
        # return res
        length = len(barcodes)
        if length < 2:
            return barcodes

        counts = {}
        max_count = 0
        for b in barcodes:
            counts[b] = counts.get(b, 0) + 1
            max_count = max(max_count, counts[b])

        evenIndex = 0
        oddIndex = 1
        half_length = length // 2
        res = [0] * length
        for x, count in counts.items():
            while count > 0 and count <= half_length and oddIndex < length:
                res[oddIndex] = x
                count -= 1
                oddIndex += 2
            while count > 0:
                res[evenIndex] = x
                count -= 1
                evenIndex += 2
        return res



Solution().rearrangeBarcodes([1, 1, 1, 2, 2, 2])
