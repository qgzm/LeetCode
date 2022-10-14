# 使用者：姜海波
# 创建时间：2022/10/15  0:21
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        mm = list(range(1, n+1))
        j = 0
        res = []
        for i in mm:
            if j < len(target):
                if i == target[j]:
                    res.append("Push")
                    j += 1
                else:
                    res.append("Push")
                    res.append("Pop")
        return res


print(Solution().buildArray([1, 3], 3))
