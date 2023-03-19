# 使用者：姜海波
# 创建时间：2023/3/19  22:33
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        minstr = s

        for k in range(n):
            s = s[ - b:] + s[: - b]
            for i in range(10):
                for j in range(n):
                    if j % 2 == 1:
                        lis = list(s)
                        lis[j] = str((int(s[j]) + a) % 10)
                        s = "".join(lis)
                if b & 1:
                    for p in range(10):
                        for q in range(n):
                            if q % 2 == 0:
                                lis = list(s)
                                lis[q] = str((int(s[q]) + a) % 10)
                                s = "".join(lis)
                        if s<minstr:
                            minstr=s
                else:
                    if s<minstr:
                        minstr=s

        return minstr


print(Solution().findLexSmallestString("74", 5, 1))
