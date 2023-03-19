# 使用者：姜海波
# 创建时间：2023/3/3  1:29
class Solution:
    def printBin(self, num: float) -> str:
        res='0.'
        while len(res)<=32 and num!=0:
            num*=2
            digit=int(num)
            res+=str(digit)
            num-=digit
        return res if len(res)<=32 else "ERROR"