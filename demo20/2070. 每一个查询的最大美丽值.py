# 使用者：姜海波
# 创建时间：2023/6/5  17:35
import collections
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x:x[0])
        n=len(items)
        for i in range(1,n):
            items[i][1]=max(items[i][1],items[i-1][1])
        def query(q):
            left,right=0,0
            while left<right:
                mid=left+(right-left)//2
                if items[mid][0]>q:
                    right=mid
                else:
                    left=mid+1
            if left==0:
                return 0
            else:
                return items[-1][1]
        ans=[query(a) for a in queries]
        return ans


Solution().maximumBeauty([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6])
