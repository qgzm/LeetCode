# 使用者：姜海波
# 创建时间：2023/3/19  17:01
from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        strin = ''
        while n > 1:
            p = n % 2
            strin = str(p)+strin
            n //= 2
        if n%2==1:
            strin='1'+strin
        strin=strin[::-1]

        for i in range(len(strin)):
            if i % 2 == 0 and strin[i] == '1':
                even += 1
            if i % 2 == 1 and strin[i] == '1':
                odd += 1

        return [even, odd]


print(Solution().evenOddBit(2))