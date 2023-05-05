# 使用者：姜海波
# 创建时间：2023/5/3  18:54
from collections import defaultdict
from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        a = defaultdict(list)
        for i in rides:
            a[i[1]].append(i)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i not in a:
                dp[i] = dp[i - 1]
                continue
            for ride in a[i]:
                start, tip = ride[0], ride[2]
                dp[i] = max(dp[i], dp[start] + i - start + tip, dp[i - 1])
        #         加dp[i]是因为到达i的位置的元素可能不止一个,此时的dp[i]还会随着遍历而更新
        return dp[-1]


print(
    Solution().maxTaxiEarnings(n=20, rides=[[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]))