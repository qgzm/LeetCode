# 使用者：姜海波
# 创建时间：2022/9/3  15:38


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 原数组被改变了
        j = 1
        k = 1
        n = len(nums)
        while j < n:
            if nums[j] > nums[j - 1]:
                nums[k] = nums[j]
                k += 1
            j += 1
        return k
