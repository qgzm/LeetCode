# 使用者：姜海波
# 创建时间：2023/4/6  12:09
import collections
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str):
            cout = collections.Counter(s)
            so = sorted(cout.items(), key=lambda x: x[0], reverse=False)
            return so[0][1]

        numb = []
        for i in words:
            numb.append(f(i))

        numb.sort()
        ans = []
        for i in queries:
            number = 0
            cnt = f(i)
            for j in numb:
                if cnt < j:
                    number += 1
            ans.append(number)
        return ans


print(Solution().numSmallerByFrequency(["bbb", "cc"], ["a", "aa", "aaa", "aaaa"]))


