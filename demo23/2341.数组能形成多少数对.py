# 使用者：姜海波
# 创建时间：2023/2/16  16:53
from collections import defaultdict
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # ans=[0]*len(nums)
        # i=0
        # while(i<len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         ans[i] = ans[i + 1] = 1
        #         i+=2
        #
        #     else:
        #         i+=1
        # sunn=sum(ans)
        # last=len(nums)-sunn
        # return [int(sunn/2),last]

        cnt = defaultdict(bool)
        res = 0
        for num in nums:
            cnt[num] = not cnt[num]
            if not cnt[num]:
                res += 1
        return [res, len(nums) - 2 * res]




print(Solution().numberOfPairs([1, 3, 2, 1, 3, 2, 2]))