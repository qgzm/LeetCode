# 使用者：姜海波
# 创建时间：2023/5/10  12:17
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans = keysPressed[0]
        maxTime = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            key = keysPressed[i]
            time = releaseTimes[i] - releaseTimes[i - 1]
            if time > maxTime or time == maxTime and key > ans:
                ans = key
                maxTime = time
        return ans

