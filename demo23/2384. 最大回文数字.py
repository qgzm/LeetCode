# 使用者：姜海波
# 创建时间：2023/4/4  11:13
import collections
from string import digits


class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt = collections.Counter(num)
        if cnt['0'] == len(num):  # 特判最特殊的情况：num 全是 0
            return "0"

        s = ""
        for d in digits[:0:-1]:
            s += d * (cnt[d] // 2)
        if s:  # 如果填了数字，则可以填 0
            s += '0' * (cnt['0'] // 2)

        t = s[::-1]
        for d in digits[::-1]:
            if cnt[d] % 2:  # 还可以填一个变成奇回文串
                s += d
                break
        return s + t  # 添加镜像部分


print(Solution().largestPalindromic('22133344'))

