# 使用者：姜海波
# 创建时间：2023/5/9  19:21
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = set()
        b = set()
        n = len(A)
        ans = []
        for i in range(n):
            a.add(A[i])
            b.add(B[i])
            c = a & b
            ans.append(len(c))
        return ans

Solution().findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4])