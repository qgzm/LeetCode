# 使用者：姜海波
# 创建时间：2023/6/5  18:25
class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        left=0
        right=x
        while left<right:
            i = (left + right) // 2
            if i*i<=x:
                ans=i
                left=i+1
            elif i*i>x:
                right=i-1
        return ans


print(Solution().mySqrt(88))
