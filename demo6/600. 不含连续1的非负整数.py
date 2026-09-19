# @Time : 2024/8/5 15:54
# @Author : 姜海波
# @Version：V 0.1
# @File : 600. 不含连续1的非负整数.py
# @desc :
from typing import List


class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0] * 31
        dp[0] = 1
        dp[1] = 1
        for i in range(2, 31):
            dp[i] = dp[i - 1] + dp[i - 2]
        pre = 0
        res = 0
        for i in range(29, -1, -1):
            val = (1 << i)
            if n & val:
                res += dp[i + 1]
                if pre == 1:
                    break
                pre = 1
            else:
                pre = 0

            if i == 0:
                res += 1
        return res

        # ans = 0
        # for i in range(n + 1):
        #     a = str(bin(i))
        #     if '11' not in a:
        #         ans += 1
        # return ans


Solution().findIntegers(5)
