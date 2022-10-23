# 使用者：姜海波
# 创建时间：2022/10/23  15:21
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "")
        number = number.replace("-", "")
        # arr=number[::-1]
        n = len(number)
        res = ""
        ran = 0
        if n % 3 == 1:
            ran = n - 4
        elif n % 3 == 0:
            ran = n - 3
        elif n % 3 == 2:
            ran = n - 2
        for i in range(ran):
            res += number[i]
            if i % 3 == 2:
                res += "-"
        if n - ran == 4:
            res += number[-4]
            res += number[-3]
            res += "-"
            res += number[-2]
            res += number[-1]
        elif n - ran == 3:
            res += number[-3:]
        elif n - ran == 2:
            res += number[-2:]
        return res


Solution().reformatNumber("1-23-45 6")
