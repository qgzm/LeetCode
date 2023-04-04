# 使用者：姜海波
# 创建时间：2023/4/4  14:32
import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = math.lcm(a, b)
        ac = math.lcm(a, c)
        bc = math.lcm(c, b)
        abc = math.lcm(a, b, c)

        def check(num):
            cnt = 0
            cnt += num // a
            cnt += num // b
            cnt += num // c
            cnt -= num // ab
            cnt -= num // ac
            cnt -= num // bc
            cnt += num // abc
            return cnt >= n

        low=1
        high=2*10**9
        while low<high-1:
            mid=low+(high-low)//2
            if check(mid):
                high=mid
            else:
                low=mid
        return low if check(low) else high



