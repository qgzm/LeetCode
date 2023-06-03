# 使用者：姜海波
# 创建时间：2023/6/3  15:29
from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        n = len(num)
        num = list(num)
        for i in range(n):
            # 寻找第一个突变后数值更大的位作为左边界
            if change[int(num[i])] > int(num[i]):
                # 尝试更新右边界
                while i < n and change[int(num[i])] >= int(num[i]):
                    num[i] = str(change[int(num[i])])
                    i += 1
                break
        return ''.join(num)