# 使用者：姜海波
# 创建时间：2023/5/6  23:20
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        lis = [0] * 5
        ans = 0
        for i in croakOfFrogs:
            if i == 'c':
                lis[0] += 1
            elif i == 'r':
                lis[1] += 1
            elif i == 'o':
                lis[2] += 1
            elif i == 'a':
                lis[3] += 1
            elif i == 'k':
                lis[4] += 1
            if not lis[0] >= lis[1] >= lis[2] >= lis[3] >= lis[4]:
                return -1
            if min(lis) > 0:
                ans = max(ans, lis[0])
                m = min(lis)
                for i in range(len(lis)):
                    lis[i] -= m

        if max(lis) == min(lis):
            return ans
        else:
            return -1
