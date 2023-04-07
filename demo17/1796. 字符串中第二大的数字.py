# 使用者：姜海波
# 创建时间：2023/4/6  21:47
class Solution:
    def secondHighest(self, s: str) -> int:
        a = b = -1
        for c in s:
            if c.isdigit():
                v = int(c)
                if v > a:
                    a, b = v, a
                elif b < v < a:
                    b = v
        return b
