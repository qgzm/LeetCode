# 使用者：姜海波
# 创建时间：2023/4/1  16:11
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # lis=[]
        # for index,integer in enumerate(nums):
        #     if integer==1:
        #         lis.append(index)
        # if len(lis)<=1:
        #     return True
        # ans=[]
        # for i in range(1,len(lis)):
        #     ans.append(lis[i]-lis[i-1])
        #
        #
        # return min(ans)>k
        prev=-1
        for index,integer in enumerate(nums):
            if integer==1:
                if prev!=-1 and index-prev-1<k:
                    return False
                prev=index
        return True


