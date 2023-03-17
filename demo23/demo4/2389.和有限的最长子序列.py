# 使用者：姜海波
# 创建时间：2023/3/17  8:41
from bisect import bisect_right
from itertools import accumulate
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        lis=list(accumulate(sorted(nums)))
        return [bisect_right(lis,q) for q in queries]