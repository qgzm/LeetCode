# 使用者：姜海波
# 创建时间：2022/10/24  17:31
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        cur_max = left_max = nums[0]
        n=len(nums)-1
        left_pos = 0
        for i in range(n):
            cur_max = max(cur_max,nums[i])
            if nums[i]<left_max:
                left_max,left_pos = cur_max, i

        return left_pos


print(Solution().partitionDisjoint([5, 0, 3, 8, 6]))