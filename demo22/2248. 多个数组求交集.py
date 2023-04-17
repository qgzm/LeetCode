# 使用者：姜海波
# 创建时间：2023/4/14  16:49
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set()
        for i in nums:
            a = set(i)
            if not ans:
                ans = a
            ans = ans & a
        return list(ans)


print(Solution().intersection(nums=[[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]))
