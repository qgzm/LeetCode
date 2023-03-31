# 使用者：姜海波
# 创建时间：2023/3/31  13:43
import collections


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ans = 0
        dic = collections.Counter(s)
        for i in dic.values():
            if i == 1:
                ans += 1
        return ans <= 1
