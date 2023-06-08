# 使用者：姜海波
# 创建时间：2023/6/7  1:18
from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        a, b, ans = arr[0], 0, arr[0]
        for i in arr[1:]:
            b = max(b + i, a)
            a = max(a + i, i)
            ans = max(ans, a, b)
        return ans
