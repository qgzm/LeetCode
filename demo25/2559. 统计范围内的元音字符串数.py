# 使用者：姜海波
# 创建时间：2023/6/2  20:44
from typing import List

# 前缀和
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n=len(words)
        sumarr=[0]*(n+1)
        for i in range(n):
            if words[i][0] in ['a','e','i','o','u'] and words[i][-1] in ['a','e','i','o','u']:
                sumarr[i+1]=sumarr[i]+1
            else:
                sumarr[i+1]=sumarr[i]
        ans=[]
        for i in range(len(queries)):
            start,end=queries[i]
            ans.append(sumarr[end+1]-sumarr[start])
        return ans