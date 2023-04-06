# 使用者：姜海波
# 创建时间：2023/4/5  14:22
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum(s[0] in "aeiou" and s[-1] in "aeiou" for s in words[left:right + 1])