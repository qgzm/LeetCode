# 使用者：姜海波
# 创建时间：2022/9/3  15:04
from cmath import inf
from typing import List

"""
要挑选最长数对链的第一个数对时，最优的选择是挑选第二个数字最小的，这样能给挑选后续的数对留下更多的空间。
挑完第一个数对后，要挑第二个数对时，也是按照相同的思路，是在剩下的数对中，第一个数字满足题意的条件下，挑选第二个数字最小的。
按照这样的思路，可以先将输入按照第二个数字排序，然后不停地判断第一个数字是否能满足大于前一个数对的第二个数字即可。
"""

class Solution(object):
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, res = -inf, 0
        # 按照pairs的第二个值排序
        for x,y in sorted(pairs,key=lambda p:p[1]):
            if cur < x:
                cur=y
                res+=1
        return res
