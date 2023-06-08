# 使用者：姜海波
# 创建时间：2023/6/5  19:29
from traitlets import Integer


class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        # return bin((A & 0xffffffff)^(B & 0xffffffff)).count('1')
        res = 0
        c = A ^ B
        for i in range(32):
            res += c >> i & 1
        return res
