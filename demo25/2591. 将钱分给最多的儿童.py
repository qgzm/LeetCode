# 使用者：姜海波
# 创建时间：2023/6/7  0:40
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money<children:
            return -1
        if money>children*8:
            return children-1
        money=money-children
        if money//7==children-1 and money%7==3:
            return children-2
        else:
            return money//7

