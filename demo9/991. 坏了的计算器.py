# 使用者：姜海波
# 创建时间：2023/4/1  15:41
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while target > startValue:
            ans += 1
            if target % 2:
                target += 1
            else:
                target //= 2
        return ans+startValue-target

