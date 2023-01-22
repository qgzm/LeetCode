# 使用者：姜海波
# 创建时间：2023/1/22  23:34
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lis = s.split()
        res = lis[:k]
        res = " ".join(res)
        return res


print(Solution().truncateSentence("Hello how are you Contestant",4))
