# @Time : 2024/8/6 18:02
# @Author : 姜海波
# @Version：V 0.1
# @File : 3084. 统计以给定字符开头和结尾的子字符串总数.py
# @desc :
from math import comb
from typing import List
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        return comb(s.count(c)+1,2)