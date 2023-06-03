# 使用者：姜海波
# 创建时间：2023/6/3  18:12
from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        count = Counter(text)
        res = 0
        for i in range(len(text)):
            j = i
            while j < len(text) and text[j] == text[i]:
                j += 1
            cur = j - i
            if cur < count[text[i]] and (j < len(text) or i > 0):
                res = max(res, cur + 1)
            k = j + 1
            while k < len(text) and text[k] == text[i]:
                k += 1
            res = max(res, min(k - i, count[text[i]]))
            i = j
        return res
