# 使用者：姜海波
# 创建时间：2023/6/1  14:47
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        dep=[]
        def dfs(rot:TreeNode,deep:int):
            if rot.left:
                dfs(rot.left,deep+1)
            if deep<len(dep):
                dep[deep]=rot.val
            else:
                dep.append(rot.val)
            if rot.right:
                dfs(rot.right,deep+1)
        dfs(root,0)

        return dep
