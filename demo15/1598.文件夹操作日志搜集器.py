# 使用者：姜海波
# 创建时间：2022/9/9  10:06
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # main=0
        log = 0
        for i in logs:
            if i == "../":
                if log > 0:
                    log -= 1
                else:
                    continue
            elif i == "./":
                continue
            else:
                log += 1
        return log
