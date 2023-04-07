# 使用者：姜海波
# 创建时间：2023/4/7  10:41
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1, b1 = map(int, num1[0:-1].split('+'))
        a2, b2 = map(int, num2[0:-1].split('+'))
        return str(a1 * a2 - b1 * b2) + '+' + str(a1 * b2 + a2 * b1) + 'i'
