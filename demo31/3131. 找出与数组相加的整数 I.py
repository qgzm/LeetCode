# @Time : 2024/8/6 18:20
# @Author : 姜海波
# @Version：V 0.1
# @File : 3131. 找出与数组相加的整数 I.py
# @desc :
from typing import List
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)