# 使用者：姜海波
# 创建时间：2022/8/31  14:10
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        lis=[]
        n=0
        for i in pushed:
            lis.append(i)
            while lis and popped[n]==lis[-1]:
                lis.pop()
                n+=1
        return n==len(popped)
if __name__=="__main__":
    # print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
