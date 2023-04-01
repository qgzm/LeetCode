# 使用者：姜海波
# 创建时间：2023/4/1  15:02
import itertools
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans=0
        for i in range(len(arr)):
            last=arr[i:]
            for j in range(len(last)+1):
                if j%2==1:
                    print(arr[i:i+j])
                    ans+=sum(arr[i:i+j])
        return ans


print(Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3]))