# 使用者：姜海波
# 创建时间：2023/5/9  19:01
from typing import List


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        i = 1
        while i * (i + 1) <= n * 2:
            i += 1
        return i - 1
