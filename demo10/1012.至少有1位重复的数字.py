# 使用者：姜海波
# 创建时间：2023/3/20  22:23
from math import perm


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        limit = list(map(int, str(n)))
        s = set()
        N = len(limit)
        # math.perm(x, i) 方法返回不重复且有顺序地从 n 项中选择 k 项的方式总数。
        # 如果 k 大于 n，则返回 0
        res = sum(9 * perm(9, i) for i in range(len(limit) - 1))
        for i, x in enumerate(limit):
            for y in range(i == 0, x):
                if y not in s:
                    res += perm(9 - i, N - i - 1)
            if x in s:
                break
            s.add(x)
        return n - res


Solution().numDupDigitsAtMostN(11)
