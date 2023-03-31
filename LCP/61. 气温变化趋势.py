# 使用者：姜海波
# 创建时间：2023/3/31  17:32
class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        diff1 = [temperatureA[i] - temperatureA[i - 1] for i in range(1, len(temperatureA))]
        diff2 = [temperatureB[i] - temperatureB[i - 1] for i in range(1, len(temperatureB))]

        res = cur = 0
        for i, j in zip(diff1, diff2):
            if i * j > 0 or i == j == 0:
                cur += 1
            else:
                cur = 0
            res = max(res, cur)
        return res