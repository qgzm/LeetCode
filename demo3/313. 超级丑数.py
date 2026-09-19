# @Time : 2024/6/26 2:15
# @Author : 姜海波
# @Version：V 0.1
# @File : 313. 超级丑数.py
# @desc :
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n + 1)
        m = len(primes)
        pointers = [0] * m  # 幂
        num = [1] * m
        for i in range(1, n + 1):
            mium = min(num)
            dp[i] = mium
            for j in range(m):
                if num[j] == mium:
                    pointers[j] += 1
                    num[j] = dp[pointers[j]] * primes[j]

        return dp[n]
