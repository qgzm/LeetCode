# 使用者：姜海波
# 创建时间：2023/5/13  14:30
import collections
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dic = dict(knowledge)
        ans, start = [], -1
        for i, c in enumerate(s):
            if c == '(':
                start = i
            elif c == ')':
                ans.append(dic.get(s[start + 1:i], "?"))
                start = -1
            elif start < 0:
                ans.append(c)
        return ''.join(ans)


print(Solution().evaluate(
    "(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]))