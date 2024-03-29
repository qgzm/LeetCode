# 使用者：姜海波
# 创建时间：2023/3/1  15:11
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        pres = {(nums[0],)}
        for i in nums[1:]:
            pres.update({j + (i,) for j in pres if j[-1] <= i})
            # 非常重要
            pres.add((i,))

        return [list(i) for i in pres if len(i) > 1]


print(Solution().findSubsequences([4, 6, 7, 7]))
