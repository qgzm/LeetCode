# 使用者：姜海波
# 创建时间：2022/12/9  19:34
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # 思想:将传过来的n转换成三进制数,如果每一位上都没有2,则表示其为3的n次幂组合而成
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3

        return True
