# 使用者：姜海波
# 创建时间：2023/5/5  8:32
from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans = 0
        begintime = 0
        id = 0
        for index, time in logs:
            if ans < time - begintime:
                ans = time - begintime
                id = index
            elif ans == time - begintime:
                id = min(id, index)
            begintime = time
        return id


print(Solution().hardestWorker(70, [[36, 3], [1, 5], [12, 8], [25, 9], [53, 11], [29, 12], [52, 14]]))
