# @Time : 2024/6/29 2:53
# @Author : 姜海波
# @Version：V 0.1
# @File : 232. 用栈实现队列.py
# @desc :
class MyQueue:

    def __init__(self):
        self.A=[]
        self.B=[]

    def push(self, x: int) -> None:
        self.A.append(x)

    def pop(self) -> int:
        peek=self.peek()
        self.B.pop()
        return peek


    def peek(self) -> int:
        if self.B:
            return self.B[-1]
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B[-1]

    def empty(self) -> bool:
        return not self.A and not self.B
