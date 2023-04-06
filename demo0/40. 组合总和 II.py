# 使用者：姜海波
# 创建时间：2023/4/5  11:32
import collections
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # def dfs(candidate: List[int], path: List[int], su):
        #     if su == target:
        #         res.append(path[:])
        #         return
        #     for i in range(len(candidate)):
        #         path.append(candidate[i])
        #         dfs(candidate[i + 1:], path, su + candidate[i])
        #         path.pop()
        #
        # res ,ans= [],[]
        # res1=[]
        # dfs(candidates, [], 0)
        # for i in res:
        #     i=sorted(i)
        #     res1.append(i)
        # res1.sort()
        # ans=[res1[0]]
        # for i in range(1,len(res1)):
        #     if ans[-1]!=res1[i]:
        #         ans.append(res1[i])
        # return ans
        def dfs(pos: int, rest: int):
            nonlocal sequence
            if rest == 0:
                ans.append(sequence[:])
                return
            if pos == len(freq) or rest < freq[pos][0]:
                return
            dfs(pos + 1, rest)
            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[:-most]

        freq = sorted(collections.Counter(candidates).items())
        ans = list()

        sequence = list()
        dfs(0, target)
        return ans


print(Solution().combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
