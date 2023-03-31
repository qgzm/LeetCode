# 使用者：姜海波
# 创建时间：2023/3/30  10:25
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        alph = {}
        ans = -1
        for i, alp in enumerate(s):
            if alp not in alph:
                alph[alp] = i
            else:
                ans = max(i - alph[alp] - 1, ans)

        return ans
