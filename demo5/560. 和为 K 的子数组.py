# 使用者：姜海波
# 创建时间：2023/6/7  0:50
import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = [0] * (len(nums) + 1)
        pre[0] = 0
        for i in range(1, len(nums) + 1):
            pre[i] = pre[i - 1] + nums[i - 1]
        dic = collections.defaultdict(int)
        ans = 0
        for j in pre:
            ans += dic[j - k]
            dic[j] += 1
        return ans


print(Solution().subarraySum(nums=[1, 1, 1], k=2))
