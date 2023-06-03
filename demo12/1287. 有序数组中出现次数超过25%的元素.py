# 使用者：姜海波
# 创建时间：2023/6/3  14:42
import collections
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        num=collections.Counter(arr)
        ma=arr[0]
        for i,j in num.items():
            if j>ma:
                ans=i
                ma=j
        return ans


print(Solution().findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))