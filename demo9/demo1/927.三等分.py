# 使用者：姜海波
# 创建时间：2022/10/6  21:42
from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        s = sum(arr)
        if s % 3:
            return [-1, -1]
        if s == 0:
            return [0, 2]
        partial = s // 3
        first = second = third = cur = 0
        # 先确定每一个数的第一个1出现的位置
        for i, x in enumerate(arr):
            if x:
                if cur == 0:
                    first = i
                elif cur == partial:
                    second = i
                elif cur == partial * 2:
                    third = i
                cur += 1
        n = len(arr)
        # 最后一个数的位数
        length = n - third
        if first + length <= second and second + length <= third:
            i = 0
            while third + i < n:
                if arr[first + i] != arr[second + i] or arr[first + i] != arr[third + i]:
                    return [-1, -1]
                i += 1

            return [first + length - 1, second + length]
        return [-1, -1]
