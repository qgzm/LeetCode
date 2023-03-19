# 使用者：姜海波
# 创建时间：2022/10/23  15:06
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        le1=len(word1)
        le2=len(word2)
        mi=min(le1,le2)
        ma=max(le1,le2)
        for i in range(mi):

            res+=word1[i]
            res+=word2[i]
        if le1>le2:
            res+=word1[mi:ma]
        else:
            res+=word2[mi:ma]
        return res


print(Solution().mergeAlternately("abc", "pqr"))