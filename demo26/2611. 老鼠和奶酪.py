# 使用者：姜海波
# 创建时间：2023/6/7  18:49
from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        arr = []
        for i in range(len(reward1)):
            arr.append(reward1[i] - reward2[i])
        arr.sort(reverse=True)
        su = sum(reward2)
        for i in range(k):
            su += arr[i]
        return su


print(Solution().miceAndCheese([4, 1, 5, 3, 3], [3, 4, 4, 5, 2], 3))