# 使用者：姜海波
# 创建时间：2023/4/6  16:33
from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        word = s.split()
        ma = 0
        for i in word:
            ma = max(ma, len(i))
        ans = list()
        for i in range(ma):
            concat = ''.join([word[i] if i < len(word) else ' ' for wo in word])
            ans.append(concat.rstrip())
        return ans
