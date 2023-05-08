# 使用者：姜海波
# 创建时间：2023/5/8  17:54
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def judge(num: int) -> int:
            i = 1
            cnt = 0
            su = 0
            while i * i <= num:
                if num % i == 0:
                    cnt += 1
                    su += i
                    if i * i != num:
                        cnt += 1
                        su += num // i
                i += 1
            if cnt == 4:
                return su
            else:
                return 0

        ans = 0
        for i in nums:
            ans += judge(i)
        return ans

Solution().sumFourDivisors([21,4,7])