# 使用者：姜海波
# 创建时间：2022/9/20  14:20
from functools import cache
from typing import List


# 又因为 n 满足1≤n≤16，所以我们可以用一个整数 S 来表示当前可用的数字集合：从低位到高位，第 ii 位为 11 则表示数字 \textit{nums}[i]nums[i]
# 可以使用，否则表示 nums[i] 已被使用。为了避免相同状态的重复计算，我们用 dp[S] 来表示在可用的数字状态为 SS
# 的情况下是否可行，初始全部状态为记录为可行状态 True。

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        al = sum(nums)
        if al % k:
            return False
        per = al // k
        nums.sort()
        if nums[-1] > per:
            return False
        n = len(nums)

        @cache
        def dfs(s, p):
            if s == 0:
                return True
            for i in range(n):
                if nums[i] + p > per:
                    break
                if s >> i & 1 and dfs(s ^ (1 << i), (p + nums[i]) % per):
                    # p + nums[i] 等于 per 时置为 0
                    return True
            return False

        return dfs((1 << n) - 1, 0)


gg = [4, 3, 2, 3, 5, 2, 1]
Solution().canPartitionKSubsets(gg, 4)
