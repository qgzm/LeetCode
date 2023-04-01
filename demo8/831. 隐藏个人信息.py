# 使用者：姜海波
# 创建时间：2023/4/2  0:38
class Solution:
    def maskPII(self, s: str) -> str:
        at = s.find('@')
        if at >= 0:
            return (s[0] + "*" * 5 + s[at - 1:]).lower()
        s = "".join(i for i in s if i.isdigit())
        return ["", "+*-", "+**-", "+***-"][len(s) - 10] + "***-***-" + s[-4:]
