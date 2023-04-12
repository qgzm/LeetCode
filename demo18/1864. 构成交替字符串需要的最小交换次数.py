# 使用者：姜海波
# 创建时间：2023/4/11  10:29
class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        n0, n1 = s.count('0'), s.count('1')
        res = float('inf')

        if n1 == (n + 1) // 2 and n0 == n // 2:
            diff1 = 0
            for i in range(n):
                if int(s[i]) == i % 2:
                    diff1 += 1
            res = min(res, diff1 // 2)

        if n0 == (n + 1) // 2 and n1 == n // 2:
            diff2 = 0
            for i in range(n):
                if int(s[i]) != i % 2:
                    diff2 += 1
            res = min(res, diff2 // 2)
        if res == float('inf'):
            return -1
        else:
            return res
