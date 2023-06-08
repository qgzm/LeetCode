# 使用者：姜海波
# 创建时间：2023/6/6  22:30
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans, sign = 0, 1
        while n:
            ans += n % 10 * sign
            sign = -sign
            n //= 10
        return ans * -sign

