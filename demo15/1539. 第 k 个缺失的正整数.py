# 使用者：姜海波
# 创建时间：2023/6/8  22:14
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in arr:
            if i <= k:
                k += 1
            else:
                break
        return k
