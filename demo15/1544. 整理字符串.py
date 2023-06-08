# 使用者：姜海波
# 创建时间：2023/6/7  19:15
class Solution:
    def makeGood(self, s: str) -> str:
        ret=list()
        for i in s:
            if ret and ret[-1].lower()==i.lower() and ret[-1]!=i:
                ret.pop()
            else:
                ret.append(i)
        return ''.join(ret)