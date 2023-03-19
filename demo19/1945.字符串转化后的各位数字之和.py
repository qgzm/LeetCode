# 使用者：姜海波
# 创建时间：2022/12/15  23:46
class Solution:
    def getLucky(self, s: str, k: int) -> int:

        dig = "".join(str(ord(ch) - ord('a') + 1) for ch in s)
        for i in range(k):
            if len(dig) == 1:
                break
            total = sum(int(ch) for ch in dig)
            dig = str(total)
        return int(dig)
