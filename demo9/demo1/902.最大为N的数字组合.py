# 使用者：姜海波
# 创建时间：2022/10/18  13:14
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # res = 0
        # le = len(digits)
        # # i记录多少位-1
        # mm=n%10
        # p=0
        # while n >= 1:
        #     m, i = 1, -1
        #     nl = n
        #     while nl // m >= 1:
        #         m *= 10
        #         i += 1
        #     m /= 10
        #     p=i
        #     while i > 0:
        #         num = nl // m
        #         first = 0
        #         for j, k in enumerate(digits):
        #             if int(k) <= num:
        #                 first = j + 1
        #                 break
        #         if first==0:
        #             first=le
        #         res += (le ** i) * first
        #         i -= 1
        #         nl = 10 ** i
        #
        #         m //= 10
        #     n%=10**(p-1)
        # for i, v in enumerate(digits): digits[i] = int(v)
        #
        # if max(digits)<=mm:
        #     res+=le
        # else:
        #     for j,k in enumerate(digits):
        #         if k>mm:
        #             first=j
        #             res+=first
        #             break
        # # for j, k in enumerate(digits):
        # #     if int(k) <= mm and int(digits[j+1])>mm:
        # #         first = j + 1
        # #         res += first
        # #         break
        # return res
        m = len(digits)
        s = str(n)
        k = len(s)
        dp = [[0, 0] for _ in range(k + 1)]
        dp[0][1] = 1
        for i in range(1, k + 1):
            for d in digits:
                if d == s[i - 1]:
                    dp[i][1] = dp[i - 1][1]
                elif d < s[i - 1]:
                    dp[i][0] += dp[i - 1][1]
                else:
                    break
            if i > 1:
                dp[i][0]+=m+dp[i-1][0]*m
        return sum(dp[k])

print(Solution().atMostNGivenDigitSet(["1", "9"], 18))
