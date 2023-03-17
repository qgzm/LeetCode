# 使用者：姜海波
# 创建时间：2023/3/17  10:34
class Solution:
    def countAndSay(self, n: int) -> str:
        def countt(strs:str):
            res=''
            count=1
            for i in range(1,len(strs)):

                if strs[i-1]==strs[i]:
                    count+=1
                else:
                    res+=str(count)+strs[i-1]
                    count=1
            res += str(count) + strs[i]
            return res

        res='1'
        if n==1:
            res='1'
        if n>1:
            res='11'
        for i in range(2,n):
            res=countt(res)

        return res


print(Solution().countAndSay(5))





