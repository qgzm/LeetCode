# 使用者：姜海波
# 创建时间：2023/2/28  0:30
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1.sort()
        items2.sort()
        m=len(items1)
        n=len(items2)
        i,j=0,0
        ret=[]
        while i<m and j<n:
            if items1[i][0]>items2[j][0]:
                ret.append([items2[j][0],items2[j][1]])
                j+=1
            elif items1[i][0]<items2[j][0]:
                ret.append([items1[i][0],items1[i][1]])
                i+=1
            else:
                ret.append([items1[i][0],items1[i][1]+items2[j][1]])
                i+=1
                j+=1
        while i<m:
            ret.append([items1[i][0],items1[i][1]])
            i+=1
        while j<n:
            ret.append([items2[j][0],items2[j][1]])
            j+=1
        # ret.sort()
        return ret


print(Solution().mergeSimilarItems([[5,1],[4,2],[3,3],[2,4],[1,5]],[[7,1],[6,2],[5,3],[4,4]]))