# 使用者：姜海波
# 创建时间：2023/4/5  14:21
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)