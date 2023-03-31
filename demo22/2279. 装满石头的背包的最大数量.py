# 使用者：姜海波
# 创建时间：2023/3/30  13:28
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n=len(capacity)
        remain=[0]*n
        for i in range(n):
            remain[i]=capacity[i]-rocks[i]
        remain.sort()
        num=0
        while additionalRocks>0 and num<n:
            # if remain[j]>0:
            additionalRocks-=remain[num]
            num+=1

        if additionalRocks>=0:
            return num
        elif additionalRocks<0:
            return num-1


print(Solution().maximumBags([91,54,63,99,24,45,78],
[35,32,45,98,6,1,25],
17))
