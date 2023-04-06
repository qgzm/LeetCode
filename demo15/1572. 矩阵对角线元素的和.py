# 使用者：姜海波
# 创建时间：2023/4/6  12:34
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = 0
        row = len(mat)
        for i in range(row):
            if row - i - 1 == i:
                n += mat[i][i]
                continue
            n += mat[i][i] + mat[row - i - 1][i]
        return n