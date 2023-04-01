# 使用者：姜海波
# 创建时间：2023/4/1  17:35
class Solution:
    def baseNeg2(self, n: int) -> str:
        res=''
        while n:
            n,k=-(n//2),n%2
            res=str(k)+res
        return res if res else '0'

