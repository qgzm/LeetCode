# 使用者：姜海波
# 创建时间：2023/6/8  0:49
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n==1 or n==2:
            return 1
        if n==3:
            return 2
        su=1
        while n>4:
            su*=3
            n-=3
        return su*n