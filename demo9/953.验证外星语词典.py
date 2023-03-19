# 使用者：姜海波
# 创建时间：2023/3/15  10:51
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dirt={}
        for i in range(len(order)):
            dirt[order[i]]=i
        for i in range(1,len(words)):
            m=len(words[i-1])
            n=len(words[i])
            minlen=min(m,n)
            mark=0
            for j in range(minlen):
                if dirt[words[i-1][j]]<dirt[words[i][j]]:
                    break
                elif dirt[words[i-1][j]]==dirt[words[i][j]]:
                    mark+=1
                else:
                    return False
            if m>n and mark==minlen:
                return False

        return True




print(Solution().isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))