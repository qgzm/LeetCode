# 使用者：姜海波
# 创建时间：2023/6/7  10:30
import collections
from typing import List


class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        ma = 0
        ans = []
        for i in range(len(points)):
            dic = collections.defaultdict(list)
            for j in range(i + 1, len(points)):
                if points[i][0] - points[j][0] == 0:
                    dic['inf'].append(j)
                else:
                    k = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    dic[k].append(j)
            for k in dic:
                if len(dic[k]) > ma:
                    ans = [i] + dic[k]
                    ma = len(dic[k])
        return ans[0:2]
