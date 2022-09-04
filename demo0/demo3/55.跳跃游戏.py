# 使用者：姜海波
# 创建时间：2022/9/4  9:03
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #贪心算法
        longest=0
        n=len(nums)
        for i in range(n):
            if i<=longest:
                longest=max(longest,i+nums[i])
                if longest>=n-1:
                    return True
        return False