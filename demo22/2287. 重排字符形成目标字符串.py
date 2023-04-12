# 使用者：姜海波
# 创建时间：2023/4/11  23:01
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        mi=max(len(s),len(target))
        for i in target:
            mi=min(mi,s.count(i)//target.count(i))
        return mi

