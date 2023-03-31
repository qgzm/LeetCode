# 使用者：姜海波
# 创建时间：2023/3/31  18:19
from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count1=Counter(word1)
        count2=Counter(word2)
        return all(abs(count1[i]-count2[2])<=3 for i in count1+count2)