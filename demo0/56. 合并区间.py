# 使用者：姜海波
# 创建时间：2023/3/29  22:53
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[intervals[0]]
        for i in range(1,len(intervals)):
            temp=ans[-1]
            leftmax=temp[1]
            rightmin=intervals[i][0]
            if leftmax>=rightmin:
                ans.pop()
                ans.append([temp[0],max(intervals[i][1],temp[1])])
            else:
                ans.append(intervals[i])

        return ans


print(Solution().merge([[1, 4], [4, 5]]))
