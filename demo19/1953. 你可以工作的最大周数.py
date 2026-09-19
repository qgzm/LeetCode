# @Time : 2024/6/29 3:41
# @Author : 姜海波
# @Version：V 0.1
# @File : 1953. 你可以工作的最大周数.py
# @desc :
from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        s = sum(milestones)
        m = max(milestones)
        return (s - m) * 2 + 1 if m > s - m + 1 else s
