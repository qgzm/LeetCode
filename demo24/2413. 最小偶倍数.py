# 使用者：姜海波
# 创建时间：2023/4/21  22:36
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * (1 + n % 2)