# 使用者：姜海波
# 创建时间：2023/4/5  15:54
from typing import List


class Solution:
    def bicycleYard(self, position: List[int], terrain: List[List[int]], obstacle: List[List[int]]) -> List[List[int]]:
        n = len(terrain)
        m = len(terrain[0])

        visit = {}
        for i in range(n):
            visit[i] = {}
            for j in range(m):
                visit[i][j] = {}

        def neighbor(pos):
            res = []
            if 0 <= pos[0] - 1 <= n - 1:
                res.append([pos[0] - 1, pos[1]])
            if 0 <= pos[0] + 1 <= n - 1:
                res.append([pos[0] + 1, pos[1]])
            if 0 <= pos[1] - 1 <= m - 1:
                res.append([pos[0], pos[1] - 1])
            if 0 <= pos[1] + 1 <= m - 1:
                res.append([pos[0], pos[1] + 1])
            return res

        def dfs(pos,speed):
            nodes=[]
            if speed<=0 or visit[pos[0]][pos[1]].get(speed,0)==1:
                return nodes
            if speed == 1:
                nodes.append(pos)
                visit[pos[0]][pos[1]][speed] = 1
            for neigh in neighbor(pos):
                h1 = terrain[pos[0]][pos[1]]
                h2 = terrain[neigh[0]][neigh[1]]
                o2 = obstacle[neigh[0]][neigh[1]]
                new_speed = speed + h1 - h2 - o2
                nodes.extend(dfs(neigh, new_speed))
            return nodes

        nodes = dfs(position, 1)

        nodes.remove(position)
        nodes.sort(key=lambda x: [x[0], x[1]])

        return nodes






