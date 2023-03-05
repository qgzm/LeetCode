# 使用者：姜海波
# 创建时间：2023/3/4  21:33
from collections import Counter
from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        # 使用二重循环枚举i和j,并使用一个长为2**16的数组存储每一种nums[i]&nums[j]以及它出现的次数
        cnt = Counter((x & y) for x in nums for y in nums)
        ans = 0
        for x in nums:
            for mask, freq in cnt.items():
                if (x & mask) == 0:
                    ans += freq
        return ans
