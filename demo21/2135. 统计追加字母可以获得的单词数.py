# 使用者：姜海波
# 创建时间：2023/4/1  23:51
from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        s = set()
        for word in startWords:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            s.add(mask)
        ans = 0
        for word in targetWords:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            for ch in word:
                if mask ^ (1 << (ord(ch) - ord('a'))) in s:
                    ans += 1
                    break
        return ans

        # # 转换成二十六位的数字
        # def mask(word: str) -> int:
        #     res = 0
        #     for ch in word:
        #         res |= 1 << (ord(ch) - ord('a'))
        #     return res
        # masks=set()
        # for start in startWords:
        #     msk=mask(start)
        #     for i in range(26):
        #         if ((msk>>i)&1)==0:
        #             masks.add(msk|(1<<i))
        # cnt=0
        # for target in targetWords:
        #     if mask(target) in masks:
        #         cnt+=1
        # return cnt
