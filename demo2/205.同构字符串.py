# 使用者：姜海波
# 创建时间：2023/3/27  14:57
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) and len(set(s)) == len(set(zip(s, t)))
