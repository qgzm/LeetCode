# 使用者：姜海波
# 创建时间：2023/3/25  0:26
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr)
        j=n-1
        while j>0 and arr[j-1]<=arr[j]:
            j-=1
        if j==0:
            return 0
        res=j
        for i in range(n):
            while j<n and arr[j]<arr[i]:
                j+=1
                # res代表后面的非递减,j-i-1代表中间删除的部分,而删中间的时候可以顺便把删前面给包括了,因为是从最左端开始的
            res=min(res,j-i-1)
            if i+1<n and arr[i]>arr[i+1]:
                break
        return res

Solution().findLengthOfShortestSubarray([1,2,3,10,4,2,3,5])