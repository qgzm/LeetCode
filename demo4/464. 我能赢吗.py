# 使用者：姜海波
# 创建时间：2023/6/7  17:54
from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # usedNumbers代表着某个数字是否被使用过,1代表使用过,0代表未使用
        @cache
        def dfs(usedNumbers: int, currentTotal: int) -> bool:
            for i in range(maxChoosableInteger):
                if (usedNumbers >> i) & 1 == 0:
                    # 这里的加一是意味着随便加个数都能赢以达到稳赢的要求
                    if currentTotal + i + 1 >= desiredTotal or \
                            not dfs(usedNumbers | (1 << i), currentTotal + i + 1):
                        return True
            return False

        return (1 + maxChoosableInteger) * maxChoosableInteger // 2 >= desiredTotal and dfs(0, 0)
