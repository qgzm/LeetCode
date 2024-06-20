# 使用者：姜海波
# 创建时间：2023/6/8  15:51
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [0]
        for num in arr:
            xor.append(xor[-1] ^ num)
        ans = list()
        for left, right in queries:
            ans.append(xor[left ^ xor[left + 1]])
        return ans
