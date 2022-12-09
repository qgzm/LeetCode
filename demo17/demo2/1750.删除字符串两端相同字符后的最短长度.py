# 使用者：姜海波
# 创建时间：2022/12/9  19:41
class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) > 1:
            a = s[0]
            b = s[-1]
            if a != b:
                return len(s)
            else:
                c = a
                while len(s)>0 and s[0] == c:
                    s=s[1:]

                while len(s)>0 and s[-1] == c:
                    s=s[:-1]

        return len(s)


print(Solution().minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"))
