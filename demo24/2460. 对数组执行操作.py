# 使用者：姜海波
# 创建时间：2023/6/5  17:31
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        return sorted(nums,key=lambda x:-bool(x))