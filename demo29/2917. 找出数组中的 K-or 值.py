# @Time : 2024/8/6 17:50
# @Author : 姜海波
# @Version：V 0.1
# @File : 2917. 找出数组中的 K-or 值.py
# @desc :
from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(31):
            cnt = sum(1 for num in nums if ((num >> i) & 1) > 0)
            if cnt >= k:
                ans |= 1 << i
        return ans
