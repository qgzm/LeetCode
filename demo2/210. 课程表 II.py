# 使用者：姜海波
# 创建时间：2023/6/3  21:56
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges=collections.defaultdict(list)
        visited=[0]*numCourses
        result=list()
        # 判断有向图中是否有环
        valid=True
        for info in prerequisites:
            edges[info[1]].append(info[0])
        def dfs(u):
            nonlocal valid
            visited[u]=1
            for v in edges[u]:
                if visited[v]==0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v]==1:
                    valid=False
                    return
            # 将节点标记为「已完成」
            visited[u]=2
            result.append()
        # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        if not valid:
            return list()
        return result[::-1]