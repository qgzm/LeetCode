# 使用者：姜海波
# 创建时间：2023/6/1  16:47
import collections
import heapq
from typing import List
from collections import defaultdict


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # ans = [0] * len(rains)
        # di = defaultdict(lambda :-1)
        # for index, value in enumerate(rains):
        #     if value > 0 and di[str(value)] == -1:
        #         # 湖满了
        #         ans[index] = -1
        #         # 记录上次湖满的天数
        #         di[str(value)] = index
        #     # 要满了,在前面寻找是否有不下雨的,最靠前最好
        #     elif value > 0 and di[str(value)]!=-1:
        #         for i in range(di[str(value)],index + 1):
        #             if i == index:
        #                 return []
        #             if ans[i] == 0:
        #                 ans[i] = value
        #                 ans[index]=-1
        #                 di[str(value)] = index
        #                 break
        #
        # for i,j in enumerate(ans):
        #     if j==0:
        #         ans[i]=1
        # return ans
        lakeToDays=collections.defaultdict(collections.deque)
        for i,r in enumerate(rains):
            if r!=0:
                lakeToDays[r].append(i)
        q=[]
        full=set()
        res=[]
        for i,r in enumerate(rains):
            if r!=0:
                if r in full:
                    return []
                else:
                    res.append(-1)
                    full.add(r)
                    lakeToDays[r].popleft()
                    if lakeToDays[r]:
                        heapq.heappush(q,lakeToDays[r][0])
            else:
                if not q:
                    res.append(1)
                else:
                    index=heapq.heappop(q)
                    res.append(rains[index])
                    full.remove(rains[index])
        return res



print(Solution().avoidFlood([1,0,2,0,3,0,2,0,0,0,1,2,3]))