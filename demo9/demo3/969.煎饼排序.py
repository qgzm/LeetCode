# 使用者：姜海波
# 创建时间：2022/10/15  12:06
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ar = arr
        res=[]
        for i in range(len(arr)):
            inde = ar.index(max(ar))
            if inde==len(ar)-1:
                ar.pop()
                continue
            else:
                ar[0:inde+1] = list(reversed(ar[0:inde+1]))
                ar.reverse()
                ar.pop()
                res.append(inde+1)
                res.append(len(ar)+1)
        return res


print(Solution().pancakeSort([3, 2, 4, 1]))