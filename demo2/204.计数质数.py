# 使用者：姜海波
# 创建时间：2023/3/26  18:37
class Solution:
    def countPrimes(self, n: int) -> int:
        def judge(m):
            for i in range(2, int(pow(m, 0.5) + 1)):
                if m % i == 0:
                    return False
            return True

        if n == 0 or n == 1:
            return 0
        ans = 0
        for i in range(2, n):

            if judge(i):
                ans += 1

        return ans


print(Solution().countPrimes(5000000))
