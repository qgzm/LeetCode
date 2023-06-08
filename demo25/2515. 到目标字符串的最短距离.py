# 使用者：姜海波
# 创建时间：2023/6/7  22:42
from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = n = len(words)
        for i, w in enumerate(words):
            if w == target:
                ans = min(ans, abs(i - startIndex), n - abs(i - startIndex))
        return ans if ans < n else -1
