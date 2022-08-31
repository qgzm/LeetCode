# 使用者：姜海波
# 创建时间：2022/8/31  19:40
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(s)
        n = len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]

        # for c in s:
        #     if i < k and (c == p[i] or p[i] == '.'):
        #         i += 1
        #     elif i < k and p[-1] == '*':
        #         return True
        #     elif i < k - 1 and p[i] == '*' and p[i + 1] != c:
        #         continue
        #     elif i < k - 1 and p[i] == '*' and p[i + 1] == c:
        #         i += 1
        #     else:
        #         return False
        # return True\
        # for c in p:
        #     if i<j and (c==s[i] or c=='.'):
        #         i+=1
        #     elif i<j and c=='*'


if __name__ == "__main__":
    s = "aa"
    p = "a"
    print(Solution().isMatch(s, p))
