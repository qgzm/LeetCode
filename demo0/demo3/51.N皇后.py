# 使用者：姜海波
# 创建时间：2022/9/3  22:08

# 方向一的斜线为从左上到右下方向，同一条斜线上的每个位置满足行下标与列下标之差相等
# 方向二的斜线为从右上到左下方向，同一条斜线上的每个位置满足行下标与列下标之和相等
# 每次放置皇后时，对于每个位置判断其是否在三个集合中，如果三个集合都不包含当前位置，则当前位置是可以放置皇后的位置。
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                # 将x列的i位置放上Q后,再复原为下一行做准备
                row[queens[i]] = 'Q'
                board.append(''.join(row))
                row[queens[i]] = '.'
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        # set的序列本身就代表行数,里面的数代表着列数
        solutions = list()
        queens = [-1] * n
        columns = set()  # columns记录每一列是否有皇后
        diagonal1 = set()  # 记录右斜方向是否有皇后
        diagonal2 = set()  # 记录左斜方向是否有皇后
        row = ['.'] * n
        backtrack(0)
        return solutions


print(Solution().solveNQueens(4))
