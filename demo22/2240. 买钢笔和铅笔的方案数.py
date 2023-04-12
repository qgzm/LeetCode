# 使用者：姜海波
# 创建时间：2023/4/7  16:08
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans=0
        num1=total//cost1
        for i in range(num1+1):
            rest=total-i*cost1
            ans+=rest//cost2+1
        return ans
