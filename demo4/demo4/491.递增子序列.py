# 使用者：姜海波
# 创建时间：2023/3/1  15:11
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # for i in range(len(nums)):
        #     tem = [nums[i]]
        #     for j in range(i + 1, len(nums)):
        #
        #         if nums[j] >= tem[-1]:
        #             tem.append(nums[j])
        #
        #             ans.append(tem)
        # return ans
        if not nums:
            return []
        pres={(nums[0],)}
        for i in nums[1:]:
            pres.update({j+(i,) for j in pres if j[-1]<=i})
            print(pres)
            pres.add((i,))
            print(pres,'ddd')

        return [list(i) for i in pres if len(i)>1]


print(Solution().findSubsequences([4, 6, 7, 7]))