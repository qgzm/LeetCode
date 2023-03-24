# 使用者：姜海波
# 创建时间：2023/3/25  2:12
from collections import Counter
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
# 判断是否大于小于k的值
        def sign(num):
            return (num>0)-(num<0)
        kIndex=nums.index(k)
        ans=0
        # 用来计算前缀和
        counts=Counter()
        counts[0]=1
        sum=0
        # 先是统计在标记前面的各种情况相当于一个"v"型,只统计y值相等的数目
        for i,num in enumerate(nums):
            sum+=sign(num-k)
            if i<kIndex:
                counts[sum]+=1
            else:
                prev0=counts[sum]
                prev1=counts[sum-1]
                ans+=prev0+prev1
        return ans


print(Solution().countSubarrays([3, 2, 1, 4, 5], 4))