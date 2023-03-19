# 使用者：姜海波
# 创建时间：2023/1/23  23:20
class Solution:
    def numSub(self, s: str) -> int:
        lis=s.split("0")
        # print(lis)
        res=0
        for i in lis:
            n=len(i)
            if n>1:
                res+=n*(n+1)/2
            elif n==1:
                res+=1
            else:
                continue
        return int(res)%(10**9+7)


print(Solution().numSub("0110111"))