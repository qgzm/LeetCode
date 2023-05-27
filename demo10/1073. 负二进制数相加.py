# 使用者：姜海波
# 创建时间：2023/5/18  21:44
from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        ans = list()

        while i >= 0 or j >= 0 or carry:
            x = carry
            if i >= 0:
                x += arr1[i]
            if j >= 0:
                x += arr2[j]

            if x >= 2:
                ans.append(x - 2)
                carry = -1
            elif x >= 0:
                ans.append(x)
                carry = 0
            else:
                ans.append(1)
                carry = 1
            i -= 1
            j -= 1

        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
        return ans[::-1]

