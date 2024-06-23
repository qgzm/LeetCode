# @Time : 2024/6/24 0:00
# @Author : 姜海波
# @Version：V 0.1
# @File : 3100. 换水问题 II.py
# @desc :

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        res = 0
        while True:
            if empty >= numExchange:
                numBottles += 1
                empty -= numExchange
                numExchange += 1


            elif numBottles > 0:
                empty += numBottles
                res += numBottles
                numBottles = 0

            else:
                return res


print(Solution().maxBottlesDrunk(numBottles=13, numExchange=6))
