# 使用者：姜海波
# 创建时间：2023/1/17  1:23
from typing import List
from collections import Counter

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # def rev(num:int):
        #     return int(str(num)[::-1])
        # res=0
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+rev(nums[j])==nums[j]+rev(nums[i]):
        #             res+=1
        # return res%(10**9+7)
        res=0
        cnt=Counter()
        for i in nums:
            j=int(str(i)[::-1])
            res+=cnt[i-j]
            cnt[i - j] += 1
        return res % (10 ** 9 + 7)



print(Solution().countNicePairs([42, 11, 1, 97]))