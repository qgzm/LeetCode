# 使用者：姜海波
# 创建时间：2023/3/15  11:53
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        judge = [[0] * n for i in range(n)]
        degree = [0] * n
        for i, j in roads:
            judge[i][j] = 1
            judge[j][i] = 1
            degree[i] += 1
            degree[j] += 1
        maxres = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = degree[i] + degree[j] - judge[i][j]
                maxres = max(maxres, res)

        return maxres
