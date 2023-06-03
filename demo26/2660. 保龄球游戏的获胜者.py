# 使用者：姜海波
# 创建时间：2023/6/3  14:03
from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(lst):
            lst = [0, 0] + lst
            return sum(lst[i] << (1 if lst[i - 1] == 10 or lst[i - 2] == 10 else 0) for i in range(2, len(lst)))

        score1, score2 = score(player1), score(player2)
        return 1 if score1 > score2 else 2 if score1 < score2 else 0

