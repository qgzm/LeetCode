# @Time : 2024/7/18 23:32
# @Author : 姜海波
# @Version：V 0.1
# @File : 3112. 访问消失节点的最少时间.py
# @desc :
from heapq import heappush, heappop
from typing import List


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v, length in edges:
            adj[u].append([v, length])
            adj[v].append([u, length])
        pq = [[0, 0]]
        answer = [-1] * n
        answer[0] = 0
        while pq:
            t, u = heappop(pq)
            if t != answer[u]:
                continue
            for v, length in adj[u]:
                if t + length < disappear[v] and (answer[v] == -1 or t + length < answer[v]):
                    heappush(pq, [t + length, v])
                    answer[v] = t + length
        return answer

Solution().minimumTime(3,[[0,1,2],[1,2,1],[0,2,4]],[1,1,5])