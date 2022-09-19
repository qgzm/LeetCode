# 使用者：姜海波
# 创建时间：2022/9/19  19:28
from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        # key是排序的依据,先是按照cnt[x]->频率排序,接着就是-x->倒序
        nums.sort(key=lambda x: (cnt[x], -x))
        return nums


aa = [1, 1, 2, 2, 2, 3]
print(Solution().frequencySort(aa))
