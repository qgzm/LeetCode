# 使用者：姜海波
# 创建时间：2023/4/7  9:51
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, z):

            if z < len(word) - 1 and board[x][y] == word[z]:
                flage[x][y] = 1
                for i, j in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                    if 0 <= i < m and 0 <= j < n and flage[i][j] == 0 :
                        dfs(i, j, z + 1)
                flage[x][y]=0
            if z == len(word) - 1 and board[x][y] == word[z]:
                flag.append(1)

        m = len(board)
        n = len(board[0])
        flag = []

        for i in range(m):
            for j in range(n):
                flage = [[0] * n for i in range(m)]
                dfs(i, j, 0)
        return True if len(flag) > 0 else False


print(Solution().exist(board=[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],word="ABCESEEEFS"))