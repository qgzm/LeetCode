# 使用者：姜海波
# 创建时间：2023/1/15  16:18
from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        le=len(nums)
        if le==1:
            return nums[0]
        elif le==2:
            return min(nums)
        else:
            newNums=[]
            i=0
            while i<le:
                if i%4==0:
                    newNums.append(min(nums[i],nums[i+1]))
                elif i%4==2:
                    newNums.append(max(nums[i],nums[i+1]))
                i+=1
            return self.minMaxGame(newNums)


print(Solution().minMaxGame([1, 3, 5, 2, 4, 8, 2, 2]))