# 使用者：姜海波
# 创建时间：2023/1/26  11:04
from string import ascii_lowercase


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        lis=[]
        for i in range(1,n+1):
            lower=max(1,k-(n-i)*26)
            k-=lower
            lis.append(ascii_lowercase[lower-1])
        return ''.join(lis)