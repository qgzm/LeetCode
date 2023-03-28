# 使用者：姜海波
# 创建时间：2023/3/28  10:57
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [*range(1-n,n,2)]

print(*range(1,4))