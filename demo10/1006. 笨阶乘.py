# 使用者：姜海波
# 创建时间：2023/3/31  20:13
class Solution:
    def clumsy(self, n: int) -> int:
        lis = []
        lis.append(n)
        n -= 1
        index = 0
        while n > 0:
            if index % 4 == 0:
                lis.append(lis.pop() * n)
            elif index % 4 == 1:
                lis.append(int(lis.pop() / float(i)))
            elif index % 4 == 2:
                lis.append(n)
            else:
                lis.append(-n)
            index += 1
            n -= 1

        summ = 0
        while len(lis) > 0:
            summ += lis.pop()

        return summ


print(Solution().clumsy(10))
