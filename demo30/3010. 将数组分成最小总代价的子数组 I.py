# @Time : 2024/8/6 17:55
# @Author : 姜海波
# @Version：V 0.1
# @File : 3010. 将数组分成最小总代价的子数组 I.py
# @desc :
from heapq import nsmallest
from typing import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return nums[0]+sum(nsmallest(2,nums[1:]))