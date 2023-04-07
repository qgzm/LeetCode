# 使用者：姜海波
# 创建时间：2023/4/7  16:07
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = 0
        sum = 0
        for i, j in enumerate(flips):
            sum += j
            if sum == (i + 2) * (i + 1) // 2:
                ans += 1
        return ans
