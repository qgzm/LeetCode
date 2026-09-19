# @Time : 2024/8/6 18:18
# @Author : 姜海波
# @Version：V 0.1
# @File : 3065. 超过阈值的最少操作数 I.py
# @desc :
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(x < k for x in nums)
