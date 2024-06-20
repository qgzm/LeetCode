# 使用者：姜海波
# 创建时间：2023/3/31  17:32
from typing import List


class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        # diff1 = [temperatureA[i] - temperatureA[i - 1] for i in range(1, len(temperatureA))]
        # diff2 = [temperatureB[i] - temperatureB[i - 1] for i in range(1, len(temperatureB))]
        #
        # res = cur = 0
        # for i, j in zip(diff1, diff2):
        #     if i * j > 0 or i == j == 0:
        #         cur += 1
        #     else:
        #         cur = 0
        #     res = max(res, cur)
        # return res
        list1 = [
            temperatureA[1] - temperatureA[i - 1] for i in range(1, len(temperatureA))
        ]
        list2 = [
            temperatureB[i] - temperatureB[i - 1] for i in range(1, len(temperatureB))
        ]
        cur = res = 0
        for i, j in zip(list1, list2):
            if i * j > 0 or i == j == 0:
                cur += 1
            else:
                cur = 0
            res = max(res, cur)
        return res

print(Solution().temperatureTrend([21,18,18,18,31],[34,32,16,16,17]))