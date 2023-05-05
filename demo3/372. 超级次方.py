# 使用者：姜海波
# 创建时间：2023/5/3  12:23
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        ans = 1
        for e in reversed(b):
            ans = ans * pow(a, e, MOD) % MOD
            a = pow(a, 10, MOD)
        return ans
