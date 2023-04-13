# 使用者：姜海波
# 创建时间：2023/4/12  23:02
import collections


class Solution:
    def digitCount(self, num: str) -> bool:
        res = collections.Counter(num)
        for i, nu in enumerate(num):
            if int(nu) != res[str(i)]:
                return False
        return True


print(Solution().digitCount("1210"))