# 使用者：姜海波
# 创建时间：2023/6/9  1:13
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(sol,nums,check):
            if len(sol)==n:
                res.append(sol)
                return
            for i in range(n):
                if check[i]==1:
                    continue
                if i>0 and nums[i]==nums[i-1] and check[i-1]==0:
                    continue
                check[i]=1
                backtrack(sol+[nums[i]],nums,check)
                check[i]=0
        nums.sort()
        res=[]
        check=[0]*(len(nums))
        n=len(nums)
        backtrack([],nums,check)
        return res
