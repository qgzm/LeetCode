# 使用者：姜海波
# 创建时间：2023/4/4  21:24
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        #  conn-同一个连通图的所有字符索引，G-邻接矩阵，- u-当前访问节点, visit-标记节点是否被访问过
        def dfs(conn, u, visit, G):
            for v in G[u]:
                if not visit[v]:
                    visit[v] = True
                    conn.append(v)
                    dfs(conn, v, visit, G)

        def bfs(conn, G, visit, u):
            queue = []
            queue.append(u)
            while queue:
                front = queue.pop(0)
                for v in G[front]:
                    visit[v] = True
                    queue.append(v)
                    conn.append(v)

        # G 邻接矩阵
        n = len(s)
        G = [[] for _ in range(n)]
        for u, v in pairs:
            G[u].append(v)
            G[v].append(u)
        # visit[i] 标记结点i是否访问过
        visit = [False] * n
        ans = list(s)
        # 如果结点u没有访问过,则遍历u所在的连通分量
        for u in range(n):
            if not visit[u]:
                conn = []
                bfs(conn, G, visit, u)
                # 对索引进行排序
                index = sorted(conn)
                # 对值进行排序
                t = sorted(ans[i] for i in conn)
                # 将排过序的值放入列表中更新
                for i, ch in zip(index, t):
                    ans[i] = ch

        return ''.join(ans)
