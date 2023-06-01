# 使用者：姜海波
# 创建时间：2023/6/1  2:25
from collections import Counter
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        cnt=Counter()
        for c in range(n - 2, 1, -1):
            cnt[nums[c + 1]] += 1
            for a in range(c):
                for b in range(a + 1, c):
                    if (total := nums[a] + nums[b] + nums[c]) in cnt:
                        ans += cnt[total]

        return ans
