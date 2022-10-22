# 使用者：姜海波
# 创建时间：2022/10/21  12:28
from cmath import inf


class StockSpanner:
    def __init__(self):
        self.stack=[(-1,inf)]
        self.idx=-1

    def next(self,price:int)->int:
        self.idx+=1
        while price>=self.stack[-1][1]:
            self.stack.pop()
        self.stack.append((self.idx,price))
        return self.idx-self.stack[-2][0]