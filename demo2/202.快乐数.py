# 使用者：姜海波
# 创建时间：2023/3/26  18:06
class Solution:
    def isHappy(self, n: int) -> bool:
        arr=set()
        while True:
            m=n
            n=0
            while m>0:
                l=m%10
                m=m//10
                n+=l**2
            if n==1:
                return True
            if n not in arr:
                arr.add(n)
            else:
                return False
