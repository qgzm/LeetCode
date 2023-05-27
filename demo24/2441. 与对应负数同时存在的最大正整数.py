# 使用者：姜海波
# 创建时间：2023/5/13  14:24
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        postive_number = set()
        nagive_number = set()
        ans = -1
        for i in nums:
            if i > 0:
                postive_number.add(i)

            else:
                nagive_number.add(i)
        for j in postive_number:
            if -j in nagive_number and j > ans:
                ans = j
        return ans
