# 使用者：姜海波
# 创建时间：2023/4/1  15:28
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        leng=len(n)
        lis=list(n)
        if n[0]!='-':
            for i,word in enumerate(lis):
                if int(word)<x:
                    return n[0:i]+str(x)+n[i:]
            return n+str(x)
        else:
            for i,word in enumerate(lis):
                if int(word)>x:
                    return n[0:i]+str(x)+n[i:]
            return n + str(x)


print(Solution().maxValue(n="99", x=9))
