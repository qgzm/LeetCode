# 使用者：姜海波
# 创建时间：2023/3/19  18:25
import sys

sys.setrecursionlimit(100000)


class Solution:
    def knightDialer(self, n: int) -> int:
        # lis = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 1]]
        # track = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
        #
        # def dfs(x, y, z,num):
        #
        #
        #     if z == n:
        #         return 1+num
        #     for i in track:
        #         mm = i[0] + x
        #         nn = i[1] + y
        #         if [mm, nn] not in lis:
        #             continue
        #         num+=dfs(mm, nn, z + 1,num)
        #     return num
        # sum=0
        # for i in lis:
        #     sum+=dfs(i[0], i[1], 1,0)
        # return sum
        MOD = 10 ** 9 + 7
        track = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        dp = [1] * 10
        for i in range(n - 1):
            dpp = [0] * 10
            for node,count in enumerate(dp):
                for n in track[node]:
                    dpp[n]+=count
                    dpp[n]%=MOD
            dp=dpp
        return sum(dp)%MOD

print(Solution().knightDialer(3))
