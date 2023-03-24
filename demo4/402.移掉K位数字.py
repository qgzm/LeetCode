# 使用者：姜海波
# 创建时间：2023/3/24  17:46
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack=[]
        for digit in num:
            while k and numStack and numStack[-1]>digit:
                numStack.pop()
                k-=1

            numStack.append(digit)
        # 如果K>0,删除末尾的k个字符
        finalStack=numStack[:-k] if k else numStack
        # 抹去前导零
        return "".join(finalStack).lstrip("0") or "0"