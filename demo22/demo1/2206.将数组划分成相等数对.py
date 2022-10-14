# 使用者：姜海波
# 创建时间：2022/10/15  1:30
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        sorted(nums)
        for i in range(len(nums)):
            if i%2==0:
                if nums[i]!=nums[i+1]:
                    return False

        return True