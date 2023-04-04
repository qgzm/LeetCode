# 使用者：姜海波
# 创建时间：2023/4/4  11:44
import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt=collections.Counter(s)
        cntsort=sorted(cnt.items(),key=lambda x:x[1],reverse=True)
        res=''
        for key,value in cntsort:
            res+=key*value

        return res


print(Solution().frequencySort("tree"))