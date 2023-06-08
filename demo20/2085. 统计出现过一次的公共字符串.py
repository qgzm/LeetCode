# 使用者：姜海波
# 创建时间：2023/6/6  21:33
import collections
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a = collections.Counter(words1)
        b = collections.Counter(words2)
        m=set()
        n=set()
        for i,j in a.items():
            if j==1:
                m.add(i)
        for i,j in b.items():
            if j==1:
                n.add(i)

        ans = 0
        for i in m:
            if i in n:
                ans += 1
        return ans


print(Solution().countWords(words1=["leetcode", "is", "amazing", "as", "is"], words2=["amazing", "leetcode", "is"]))