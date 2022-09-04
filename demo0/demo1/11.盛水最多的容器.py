# 使用者：姜海波
# 创建时间：2022/9/2  19:12

# 重要一点在于,将较小边进行挪动,这样 才 可能获得 最优解,不然挪动最长边只会是较差的解

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxv = 0
        n = len(height)
        j = n - 1
        i = 0
        while i < j:
            # maxv=max(maxv,height[i]*(i+1))
            s = min(height[i], height[j]) * (j - i)
            maxv = max(s, maxv)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxv


lis = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(lis))
