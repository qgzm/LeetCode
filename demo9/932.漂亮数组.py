# 使用者：姜海波
# 创建时间：2023/3/27  22:16
from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        memo={1:[1]}
        def f(N):
            if N not in memo:
                odds=f((N+1)//2)
                evens=f(N//2)
                memo[N]=[2*x-1 for x in odds]+[2*x for x in evens]

            return memo[N]
        return f(n)