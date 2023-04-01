# 使用者：姜海波
# 创建时间：2023/4/1  11:59
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def dfs(strin: List[str], i):
            while i < len(strin) and s[i].isdigit():
                i += 1
            if i == len(s):
                ans.append(''.join(strin))
                return
            dfs(strin, i + 1)
            strin[i] = strin[i].swapcase()
            dfs(strin, i + 1)
            strin[i] = strin[i].swapcase()

        dfs(list(s), 0)
        return ans
