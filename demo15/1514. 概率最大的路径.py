# 使用者：姜海波
# 创建时间：2023/6/8  15:02
import collections
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        if not edges or not edges[0]:
            return 0
        st = collections.defaultdict(list)
        for i, (s, e) in enumerate(edges):
            st[s].append((e, succProb[i]))
            st[e].append((s, succProb[i]))
        ans = 0
        queue = collections.deque([(start, 1)])
        visited = {start: 0}
        while queue:
            node, dis = queue.popleft()
            for next, d in st[node]:
                nextd = dis * d
                if next == end:
                    ans = max(ans, nextd)
                    continue
                if nextd > ans and (next not in visited or visited[next] < nextd):
                    visited[next] = nextd
                    queue.append((nextd, nextd))
        return ans
