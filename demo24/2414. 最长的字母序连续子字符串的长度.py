# 使用者：姜海波
# 创建时间：2023/4/6  12:27
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        res = 1
        winLen = 1
        for i in range(1, n):
            if ord(s[i]) - ord(s[i - 1]) == 1:
                winLen += 1
            else:
                winLen = 1
            res = max(res, winLen)

        return res