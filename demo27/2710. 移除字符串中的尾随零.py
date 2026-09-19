# @Time : 2024/6/29 1:49
# @Author : 姜海波
# @Version：V 0.1
# @File : 2710. 移除字符串中的尾随零.py
# @desc :
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        n = len(num)
        while n > 0 and num[n - 1] == '0':
            n -= 1
        return num[0 : n]