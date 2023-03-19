# 使用者：姜海波
# 创建时间：2022/10/20  8:42
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        return (k&1)^1^self.kthGrammar(n-1,(k+1)//2)