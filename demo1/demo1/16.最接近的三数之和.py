# 使用者：姜海波
# 创建时间：2022/9/1  15:40
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ret = float('inf')
        nums.sort()
        for i in range(n - 2):
            l = i + 1
            r = n - 1

            while l < r:
                m = nums[r] + nums[i] + nums[l]
                ret = m if abs(target - m) < abs(ret - target) else ret
                if m == target:
                    return target
                if m > target:
                    r -= 1
                else:
                    l += 1
        return ret
