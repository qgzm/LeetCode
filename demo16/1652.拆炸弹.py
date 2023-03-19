# 使用者：姜海波
# 创建时间：2022/9/24  20:02
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        m = len(code)
        re = []
        if k > 0:
            for i in range(m):
                d = 0
                for j in range(1, k + 1):
                    a = (i + j) % m

                    d += code[a]
                re.append(d)
        elif k == 0:
            for i in range(m):
                re.append(0)
        else:
            for i in range(m):
                c = 0
                for j in range(1, abs(k) + 1):
                    a = (i - j + m) % m;

                    c += code[a]
                re.append(c)
        return re
