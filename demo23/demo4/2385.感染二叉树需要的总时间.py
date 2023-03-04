# 使用者：姜海波
# 创建时间：2023/3/1  18:13
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # li=[0]*len(root)
        # ans=0
        # num=0
        # for i in range(len(root)):
        #     if start==root[i]:
        #         li[i]=1
        #     if root[i]=='null':
        #         li[i]=-1
        #
        # while True:
        #     ans+=1
        #     for i in range(len(root)):
        #         if i ==1:
        #             if 2*i+1<len(root) and li[2*i+1]==0:
        #                 li[2*i+1]=1
        #             if 2*i+2<len(root) and li[2*i+2]==0:
        #                 li[2*i+2]=1
        #             if li[(i+1)//2]==0:
        parents={}
        def dfs(node:Optional[TreeNode],pa:Optional[TreeNode])->None:
            if node is None:
                return
            if node.val==start:
                self.start=node
            parents[node]=pa
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root,None)

        ans=-1
        vis={None,self.start}
        q=[self.start]
        while q:
            ans+=1
            tmp=q
            q=[]
            for node in tmp:
                for x in node.left,node.right,parents[node]:
                    if x not in vis:
                        vis.add(x)
                        q.append(x)
        return ans









