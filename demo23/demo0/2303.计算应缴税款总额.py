# 使用者：姜海波
# 创建时间：2023/1/23  1:44
from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        num = 0
        for i in brackets:
            if i[0] < income:
                num += 1
            else:

                break
        sum = 0
        if num == 0:
            return income * brackets[0][1] / 100

        for j in range(num):
            if j == 0:
                sum += brackets[j][0] * brackets[j][1] / 100
            else:
                sum += (brackets[j][0] - brackets[j - 1][0]) * brackets[j][1] / 100
        sum += (income - brackets[num - 1][0]) * brackets[num][1] / 100

        return sum


print(Solution().calculateTax([[3, 50], [7, 10], [12, 25]], 10))
