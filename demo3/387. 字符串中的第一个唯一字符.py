# 使用者：姜海波
# 创建时间：2023/3/30  11:09
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = collections.Counter(s)
        for i, ch in enumerate(frequency):
            if frequency[ch] == 1:
                return i
        return -1
