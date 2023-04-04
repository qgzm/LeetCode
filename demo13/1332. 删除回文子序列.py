# 使用者：姜海波
# 创建时间：2023/4/4  14:17
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2