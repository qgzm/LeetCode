# 使用者：姜海波
# 创建时间：2023/5/30  18:38
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index = {p[0]: i for i, p in enumerate(pieces)}
        i = 0
        while i < len(arr):
            if arr[i] not in index:
                return False
            p = pieces[index[arr[i]]]
            if arr[i:i + len(p)] != p:
                return False
            i += len(p)
        return True

Solution().canFormArray([91,4,64,78],[[78],[4,64],[91]])