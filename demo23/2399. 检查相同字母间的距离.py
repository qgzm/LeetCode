# 使用者：姜海波
# 创建时间：2023/4/9  11:57
from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j] and distance[ord(s[i]) - ord('a')] != j - i - 1:
                    return False
        return True

   