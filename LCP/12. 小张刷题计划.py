# 使用者：姜海波
# 创建时间：2023/6/4  18:44
from typing import List


class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        def check(limit, cost, day):
            useday, totaltime, maxtime = 1, 0, cost[0]
            for i in cost[1:]:
                if totaltime + min(maxtime, i) <= limit:
                    totaltime, maxtime = totaltime + min(maxtime, i), max(maxtime, i)
                else:
                    useday += 1
                    totaltime, maxtime = 0, i
            return useday <= day

        if len(time) < m:
            return 0
        l, r = 0, sum(time)
        while l < r:
            mid = (l + r) >> 1
            if check(mid, time, m):
                r = mid
            else:
                l = mid
        return l
