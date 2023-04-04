# 使用者：姜海波
# 创建时间：2023/4/3  15:20
from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        m = arr[-1]
        for i in range(n - 2, -1, -1):
            if m < arr[i]:
                for j in range(n - 1, i, - 1):
                    if arr[j] < arr[i] and arr[j] >= m:
                        p, m = j, arr[j]
                arr[i], arr[p] = arr[p], arr[i]
                break
            m = min(m, arr[i])
        return arr
