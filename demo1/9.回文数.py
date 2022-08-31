# 使用者：姜海波
# 创建时间：2022/8/29  21:58
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        quo = x
        y = 0
        while (quo != 0):
            remainder = quo % 10
            y = y * 10 + remainder
            quo = quo // 10
        return y == x

