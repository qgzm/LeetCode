# 使用者：姜海波
# 创建时间：2023/4/5  21:15
from math import gcd

# x是a和b的公因子，当且仅当x是a和b的最大公约数的因子
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c, ans = gcd(a, b), 0
        x = 1
        while x * x <= c:
            if c % x == 0:
                ans += 1
                if x * x != c:
                    ans += 1
            x += 1
        return ans
