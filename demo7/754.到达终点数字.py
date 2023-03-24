# 使用者：姜海波
# 创建时间：2023/3/24  14:42
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        i = 0
        allsum = 0
        while (allsum < target):
            i += 1
            allsum += i

        t = allsum - target
        if t % 2 == 0:
            return i
        else:
            if i % 2 == 0:
                return i + 1
            else:
                return i + 2
