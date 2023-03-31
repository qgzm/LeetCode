# 使用者：姜海波
# 创建时间：2023/3/30  10:45
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1=set(nums1)
        set2=set(nums2)
        set3=set(nums3)

        a=set1&set2
        b=set2&set1
        c=set1&set3
        d=set2&set3
        e=set3&set1
        f=set3&set2
        return list(a|b|c|d|e|f)


print(Solution().twoOutOfThree(nums1=[1, 1, 3, 2], nums2=[2, 3], nums3=[3]))