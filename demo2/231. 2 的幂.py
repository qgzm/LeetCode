# 使用者：姜海波
# 创建时间：2023/5/9  16:10
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        a=bin(n)
        b=a[2:]
        if b=='1' or (b[0]=='1' and int(b[1:])==0):
            return True
        else:
            return False



print(Solution().isPowerOfTwo(16))