# 使用者：姜海波
# 创建时间：2023/3/31  13:54
from typing import List


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        sum1=sum(array1)
        sum2=sum(array2)
        m,n=len(array1),len(array2)
        diff=sum2-sum1
        array1.sort()
        array2.sort()
        if diff%2==1:
            return []
        else:
            for i in array1:
                if i+diff//2 in array2:
                    return [i,i+diff//2]
            return []