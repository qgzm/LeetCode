# 使用者：姜海波
# 创建时间：2023/5/29  22:51
from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ave = 0
        cnt = 0
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                ave += i
                cnt += 1
        if cnt == 0:
            return 0
        return ave // cnt


Solution().averageValue(nums = [1,2,4,7,10])