# 使用者：姜海波
# 创建时间：2023/3/17  10:04
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        length=len(tokens)
        token=[]
        for i in range(length):
            if tokens[i] in ['+','-','*','/']:
                aa=str(int(eval(token[-2]+tokens[i]+token[-1])))
                token.pop()
                token.pop()
                token.append(aa)
            else:
                token.append(tokens[i])

        return int(token[0])


print(Solution().evalRPN(["4","13","5","/","+"]))