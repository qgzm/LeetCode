# 使用者：姜海波
# 创建时间：2023/5/23  15:10
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 1 % k
        le = 1
        se = set()
        se.add(remainder)
        while remainder != 0:
            remainder = (remainder * 10 + 1) % k
            le += 1

            if remainder in se:
                return -1
            se.add(remainder)
        return le
