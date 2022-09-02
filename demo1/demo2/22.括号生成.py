# 使用者：姜海波
# 创建时间：2022/9/2  19:53
from typing import List


# 回溯法
# 只在序列仍然保持有效时才添加(或者)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)  # 回溯
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans


print(Solution().generateParenthesis(3))
