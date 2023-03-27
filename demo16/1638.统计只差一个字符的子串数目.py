# 使用者：姜海波
# 创建时间：2023/3/27  10:42
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        m = len(s)
        n = len(t)
        for i in range(m):
            for j in range(n):
                diff = 0
                k = 0  # 子串的长度
                while i + k < m and j + k < n:
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff == 1:
                        ans += 1
                    elif diff > 1:
                        break
                    k += 1

        return ans
