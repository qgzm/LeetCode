# 使用者：姜海波
# 创建时间：2023/3/31  10:45
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int) -> None:
            d = k - len(path)
            if d == 0:
                ans.append(path.copy())
                return
            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1)
                path.pop()

        dfs(n)
        return ans


print(Solution().combine(4, 2))
