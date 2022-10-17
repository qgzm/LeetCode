# 使用者：姜海波
# 创建时间：2022/10/17  7:49
from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        # ma = 0
        # k=0
        # for i in range(len(fruits)):
        #     if i!=k:
        #         continue
        #     j = i
        #     while fruits[j] == fruits[i]:
        #         j += 1
        #         if j >= len(fruits):
        #             j -= 1
        #             le=j-i+1
        #             break
        #
        #     if i!=j:
        #         k = j
        #         le = j - i
        #         while fruits[i] == fruits[k] or fruits[j] == fruits[k]:
        #             k += 1
        #             le += 1
        #             if k >= len(fruits):
        #                 break
        #     ma = max(ma, le)
        cnt = Counter()
        left = ans = 0
        for right, x in enumerate(fruits):
            cnt[x]+=1
            while len(cnt)>2:
                cnt[fruits[left]]-=1
                if cnt[fruits[left]]==0:
                    cnt.pop(fruits[left])
                left+=1
            ans=max(ans,right-left+1)

        return ans


print(Solution().totalFruit([0,1,2,2]))