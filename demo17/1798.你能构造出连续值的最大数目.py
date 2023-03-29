# 使用者：姜海波
# 创建时间：2023/3/29  15:16
from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        canGet=0
        for i in coins:
            if i<=canGet:
                canGet+=i
            else:
                break
        return canGet+1