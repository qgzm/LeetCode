# 使用者：姜海波
# 创建时间：2023/4/6  20:34
from math import floor, sqrt
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        numsset=set(nums)
        flag=[0]*len(nums)
        ans=0
        repetition=set()
        for i in nums:
            if i not in repetition:
                repetition.add(i)
                jude=True
                res=1
                j=i
                while jude:
                    if j**2 in numsset:
                        j=j**2
                        repetition.add(j)
                        res+=1
                    else:
                        break

                while jude:
                    if floor(sqrt(i)+0.5)==sqrt(i) and int(sqrt(i)) in numsset:
                       i=int(sqrt(i))
                       repetition.add(i)
                       res+=1
                    else:
                        break
                ans=max(res,ans)

        return ans if ans>1 else -1


print(Solution().longestSquareStreak(nums = [2,3,5,6,7]))