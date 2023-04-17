# 使用者：姜海波
# 创建时间：2023/4/14  16:25
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def fun(st: str, pat: str):
            j = 0
            for i in st:
                if i == pat[j]:
                    j += 1
                    if j == len(pat):
                        return True
                    continue
                if i.isupper():
                    return False
                else:
                    continue

        ans = []
        for i in queries:

            if fun(i, pattern):
                ans.append(True)
            else:
                ans.append(False)
        return ans
