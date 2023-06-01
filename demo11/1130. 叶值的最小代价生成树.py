# 使用者：姜海波
# 创建时间：2023/6/1  0:35
from cmath import inf
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[[inf for i in range(n)] for j in range(n)]
        mval=[[0 for i in range(n)] for j in range(n)]
        for j in range(n):
            mval[j][j]=arr[j]
            dp[j][j]=0
            for i in range(j-1,-1,-1):
                mval[i][j]=max(arr[i],mval[i+1][j])
                for k in range(i,j):
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+mval[i][k]*mval[k+1][j])
        return dp[0][n-1]


print(Solution().mctFromLeafValues([6, 2, 4]))