# 使用者：姜海波
# 创建时间：2023/3/3  23:25
from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        dic = {}
        for i in names:
            if i not in ans:
                ans.append(i)
            else:
                k = 1
                while i in ans:
                    i = i + "(" + str(k) + ")"
