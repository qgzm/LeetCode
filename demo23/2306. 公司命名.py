# 使用者：姜海波
# 创建时间：2023/5/5  18:11
from collections import defaultdict
from itertools import combinations
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # ans = 0
        # for i in combinations(ideas, 2):
        #     a = i[0][0] + i[1][1:]
        #     b = i[1][0] + i[0][1:]
        #     if a not in ideas and b not in ideas:
        #         ans += 1
        # return ans * 2
        group = defaultdict(set)
        for s in ideas:
            group[s[0]].add(s[1:])
        ans = 0
        for a, b in combinations(group.values(), 2):
            # m是交集,要去掉
            m = len(a & b)
            ans += (len(a) - m) * (len(b) - m)
        return ans * 2


print(Solution().distinctNames(ideas = ["coffee","donuts","time","toffee"]))