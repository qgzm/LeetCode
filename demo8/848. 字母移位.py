# 使用者：姜海波
# 创建时间：2023/6/3  14:08
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        dp=[]
        stri=list(s)
        for i in range(len(shifts)):
            dp.append(sum(shifts[i:]))
        for i in range(len(shifts)):
            stri[i]=chr((ord(stri[i])+dp[i]-ord('a'))%26+ord('a'))
        return ''.join(stri)

