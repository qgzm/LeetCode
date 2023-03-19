# 使用者：姜海波
# 创建时间：2022/10/9  22:12
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # n = len(s)
        # if n == 2:
        #     return 1
        # bal = 0
        # for i, c in enumerate(s):
        #     bal += 1 if c == '(' else -1
        #     if bal == 0:
        #         if i == n - 1:
        #             return 2 * self.scoreOfParentheses(s[1:-1])
        #         return self.scoreOfParentheses(s[:i + 1]) + self.scoreOfParentheses(s[i + 1:])
        st = [0]
        for c in s:
            if c == '(':
                st.append(0)
            else:
                v = st.pop()
                st[-1] += max(2 * v, 1)
        return st[-1]
"""
    遇到左括号，那么我们需要计算该左括号内部的子平衡括号字符串 AA 的分数，我们也要先压入分数 00，表示 AA 前面的空字符串的分数。

    遇到右括号，说明该右括号内部的子平衡括号字符串 AA 的分数已经计算出来了，我们将它弹出栈，并保存到变量 vv 中。
    如果 v = 0v=0，那么说明子平衡括号字符串 AA 是空串，(A)(A) 的分数为 11，否则 (A)(A) 的分数为 2v2v，然后将 (A)(A) 的分数加到栈顶元素上。

"""

