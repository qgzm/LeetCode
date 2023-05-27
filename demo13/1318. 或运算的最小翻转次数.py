# 使用者：姜海波
# 创建时间：2023/5/25  17:32
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        d = (a | b) ^ c
        return bin(d).count('1') + bin(a & b & d).count('1')
