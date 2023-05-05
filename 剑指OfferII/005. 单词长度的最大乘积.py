# 使用者：姜海波
# 创建时间：2023/5/2  23:37
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # 位掩码
        # 将单词转换成二进制数字，然后进行与运算
        masks = []
        fun = lambda a, b: a | (1 << (ord(b) - ord('a')))
        for i in words:
            num = 0
            for j in i:
                num = fun(num, j)
            masks.append(num)
        lenmax = 0
        for x, y in itertools.product(zip(masks, words), repeat=2):
            if x[0] & y[0] == 0:
                lenmax = max(len(x[1]) * len(y[1]), lenmax)
        return lenmax


