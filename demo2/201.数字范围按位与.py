# 使用者：姜海波
# 创建时间：2023/3/26  17:58
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 寻找公共前缀
        shift = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift
#     while left<right:
#          n=n&(n-1)
#      return n
