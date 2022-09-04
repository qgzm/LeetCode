# 使用者：姜海波
# 创建时间：2022/9/4  9:33
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        for i, row in enumerate(mat):
            # 用第一行存储数据,当第一行
            cnt = sum(row) - (i == 0)
            if cnt:
                for j, x in enumerate(row):
                    if x == 1:
                        mat[0][j] += cnt
        # 定义第 j 列的标记值为：该列所有 1 所在行中的 1 的数量之和。
        return sum(x == 1 for x in mat[0])


#         m=len(mat)
#         n=len(mat[0])
#         x=list()
#         y=list()
#         for i in range(m):
#             num=0
#             for j in range(n):
#                 if mat[i][j]==1:
#                     num+=1
#             x.append(num)
#         for i in range(m):
#             num=0
#             for j in range(n):
#                 if mat[j][i]==1:
#                     num+=1
#             y.append(num)

        # rows_sum = [sum(row) for row in mat]
        # cols_sum = [sum(col) for col in zip(*mat)]
#         res=0
#         for i, row in enumerate(mat):
#             for j, x in enumerate(row):
#                 if x == 1 and rows_sum[i] == 1 and cols_sum[j] == 1:
#                     res += 1
#         return res
a = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
print(Solution().numSpecial(a))


