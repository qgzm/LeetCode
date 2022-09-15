# 使用者：姜海波
# 创建时间：2022/9/14  9:20
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        m = len(arr) * 0.05
        m=int(m)
        for i in range(m):
            arr.pop()

        arr.sort(reverse=True)
        for i in range(m):
            arr.pop()
        n = len(arr)
        nums = 0
        for i in range(n):
            nums += arr[i]

        return nums / n
