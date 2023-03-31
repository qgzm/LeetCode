# 使用者：姜海波
# 创建时间：2023/3/31  14:41
from collections import Counter
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        cnt = Counter()
        for i in nums:
            res += cnt[i - k] + cnt[i + k]
            cnt[i] += 1

        return res
