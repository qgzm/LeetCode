# 使用者：姜海波
# 创建时间：2023/4/29  21:37
import collections


class Solution:
    def equalFrequency(self, word: str) -> bool:
        dic = collections.Counter(word)
        ans = []
        for i in dic.values():
            ans.append(i)
        ans.sort()
        if (len(ans) > 1 and ans[0] == ans[-1] == 1) or len(ans)==1:
            return True
        if len(ans) >= 2 and ans[0] == ans[-1]:
            return False
        di=collections.Counter(ans)
        if len(di)>2:
            return False
        lis=[]
        ls=[]
        for i in di.values():
            lis.append(i)
        if lis[0]>1 and lis[1]>1:
            return False
        for i in di.keys():
            ls.append(i)
        if abs(ls[0]-ls[1])>1:
            return False
        if di[max(ls)] > 1:
            return False
        return True


print(Solution().equalFrequency("aaaabbbbccc"))