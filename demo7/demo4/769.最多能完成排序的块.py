# 使用者：姜海波
# 创建时间：2022/10/13  9:41
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        maxth = 0
        # 当遍历到第i个位置的时候,如果可以切分为块,那么前i个位置的最大值一定等于i
        # 否则,一定有比i小的数划分到后面的块,那块排序后,一定不满足升序
        for i in range(len(arr)):
            maxth = max(maxth, arr[i])
            if maxth == i:
                res += 1
        return res

Solution().maxChunksToSorted([4,3,2,1,0])