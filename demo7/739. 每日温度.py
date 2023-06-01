# 使用者：姜海波
# 创建时间：2023/5/30  14:25
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr=[0]*len(temperatures)
        for i in range(len(temperatures)-2,-1,-1):
            if temperatures[i]<=temperatures[i+1]:
                arr[i]=1
            else:
                j=i+1


                while temperatures[i]>temperatures[j]:
                    if arr[j] == 0:
                        arr[i] = 0
                        break
                    j+=arr[j]
                arr[i]=j-i

        return arr
