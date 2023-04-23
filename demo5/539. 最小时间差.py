# 使用者：姜海波
# 创建时间：2023/4/18  21:54
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 24 * 60:
            return 0
        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        minutes.append(minutes[0] + 24 * 60)
        return min(minutes[i] - minutes[i - 1] for i in range(1, len(minutes)))