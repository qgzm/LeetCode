# 使用者：姜海波
# 创建时间：2023/3/4  21:51
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        n,m=len(board),len(board[0])


        def dfs(x,y):
            if not 0<=x<n or not 0<=y <m or board[x][y]!="O":
                return
            board[x][y]='Y'
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)

        for i in range(n):
            dfs(i,0)
            dfs(i,m-1)

        for i in range(m-1):
            dfs(0,i)
            dfs(n-1,i)

        for i in range(n):
            for j in range(m):
                if board[i][j]=="Y":
                    board[i][j]="O"
                elif board[i][j]=='O':
                    board[i][j]='X'
