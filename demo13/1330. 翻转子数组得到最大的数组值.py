# 使用者：姜海波
# 创建时间：2023/5/12  22:10
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        value, n = 0, len(nums)
        for i in range(n - 1):
            value += abs(nums[i] - nums[i + 1])
        mx1 = 0
        for i in range(1, n - 1):
            mx1 = max(mx1, abs(nums[0] - nums[i + 1]) - abs(nums[i] - nums[i + 1]))
            mx1 = max(mx1, abs(nums[-1] - nums[i - 1]) - abs(nums[i] - nums[i - 1]))
        mx2, mn2 = -inf, inf
        for i in range(n - 1):
            x, y = nums[i], nums[i + 1]
            mx2 = max(mx2, min(x, y))
            mn2 = min(mn2, max(x, y))
        return value + max(mx1, 2 * (mx2 - mn2))

