# 使用者：姜海波
# 创建时间：2023/5/5  17:49
from typing import List


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        res = []
        for l, r in queries:
            a = bin(l ^ r).removeprefix('0b')
            pos = s.find(a)
            res.append([pos, -1 if pos == -1 else pos + len(a) - 1])
        return res
