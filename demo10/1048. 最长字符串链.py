# 使用者：姜海波
# 创建时间：2023/4/27  1:55
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for word in sorted(words, key=len):
            dp[word] = max(dp.get(word[0:i] + word[i + 1:], 0) + 1 for i in range(len(word)))
        return max(dp.values())
