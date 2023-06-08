# 使用者：姜海波
# 创建时间：2023/6/5  20:37
import collections
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic=collections.defaultdict()
        index=[]
        for i in range(26):
            if s.count(chr('a'+i)):
                index.append([s.find(chr('a'+i)),s.rfind('a'+i)])
        index.sort()
        left=index[0][0]
        right=index[0][1]
        res=list()
        for i in index:
            if i[0]<=right:
                right=max(right,i[1])
            else:
                res.append([left,right])
                left=i[0]
                right=i[1]
        res.append([left,right])
        return [re[1]-re[0]+1 for re in res ]

