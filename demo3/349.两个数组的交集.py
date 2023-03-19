# 使用者：姜海波
# 创建时间：2022/12/9  0:55
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=set(nums1)
        b=set(nums2)
        c=list(a-(a-b))
        return c



a=set((1,2,3))
b=set((2,3,4))
c=a-(a-b)
print(list(c))