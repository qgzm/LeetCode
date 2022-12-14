# 使用者：姜海波
# 创建时间：2022/9/3  17:20
from typing import List

#优化,不用eval,直接append元素,然后if xx in arr判断是否在里面
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(9):
                if board[i][j] != '.':
                    m = eval(board[i][j])
                    arr[m] += 1
            if max(arr) >= 2:
                return False
        for i in range(9):
            arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(9):
                if board[j][i] != '.':
                    m = eval(board[j][i])
                    arr[m] += 1
            if max(arr) >= 2:
                return False
        m, n = 0, 0
        for i in range(3):
            m = i * 3
            for j in range(3):
                n = j * 3
                arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                for k in range(3):
                    for l in range(3):
                        if board[m + k][n + l] != '.':
                            p = eval(board[m + k][n + l])
                            arr[p] += 1
                if max(arr) >= 2:
                    return False
        return True


# tt=[[".",".",".",".","5",".",".","1","."],
#     [".","4",".","3",".",".",".",".","."],
#     [".",".",".",".",".","3",".",".","1"],
#     ["8",".",".",".",".",".",".","2","."],
#     [".",".","2",".","7",".",".",".","."],
#     [".","1","5",".",".",".",".",".","."],
#     [".",".",".",".",".","2",".",".","."],
#     [".","2",".","9",".",".",".",".","."],
#     [".",".","4",".",".",".",".",".","."]]
tt = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
      [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
      ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
      [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
      [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().isValidSudoku(tt))
