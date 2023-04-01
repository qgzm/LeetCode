# 使用者：姜海波
# 创建时间：2023/4/1  17:56
class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ''
        flag = 0
        if num < 0:
            flag = 1
            num = -num
        while num:
            num, k = num // 7, num % 7
            res = str(k) + res
        if flag == 1:
            return '-' + res
        elif res:
            return res
        else:
            return '0'