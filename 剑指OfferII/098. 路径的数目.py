# 使用者：姜海波
# 创建时间：2023/3/31  8:50
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==n==1:
            return 1
        arr=[[0]*n]*m
        for i in range(m):
            arr[i][0]=1
        for j in range(n):
            arr[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                arr[i][j]=arr[i-1][j]+arr[i][j-1]
        return arr[-1][-1]


print(Solution().uniquePaths(3, 7))