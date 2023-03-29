# 使用者：姜海波
# 创建时间：2023/3/29  23:18
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic={}
        for i in range(len(nums)):
            if target-nums[i] not in dic:
                dic[nums[i]]=i
            else:
                return [dic[target-nums[i]],i]

        return []


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))