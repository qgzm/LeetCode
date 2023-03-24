# 使用者：姜海波
# 创建时间：2023/3/24  16:24
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        people=sorted(zip(ages,scores))

        dp=[0]*len(scores)
        for i in range(len(people)):
            dp[i]=people[i][1]
            for j in range(i):
                if people[j][1]<=people[i][1]:
                    dp[i]=max(dp[i],dp[j]+people[i][1])

        return max(dp)


print(Solution().bestTeamScore([1,3,7,3,2,4,10,7,5],[4,5,2,1,1,2,4,1,4]))