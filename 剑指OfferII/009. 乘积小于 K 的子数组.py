# 使用者：姜海波
# 创建时间：2023/6/7  19:31
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        left, right = 0, 0
        n = len(nums)
        ans = 0
        mul = 1
        while left < n:
            if left>right:
                right=left
                mul=1
            while mul < k and right<=n:
                if right < n:
                    mul *= nums[right]

                    right += 1
                else:
                    right+=1
                    break
            if right>left:
                ans += right - left - 1
            else:
                ans+=0
            mul //= nums[left]
            left += 1

            # if right < n - 1:
            #     right += 1
        return ans


print(Solution().numSubarrayProductLessThanK(nums=[1,1,1], k=1))
