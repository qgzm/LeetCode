# 使用者：姜海波
# 创建时间：2023/6/1  14:12
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(rot: Optional[TreeNode], deep: int):
            if deep>=2 and deep == depth - 1:
                aa = rot.left
                rot.left = TreeNode(val)
                rot.left.left = aa
                bb = rot.right
                rot.right = TreeNode(val)
                rot.right.right = bb
                return
            if rot.left:
                dfs(rot.left, deep + 1)
            if rot.right:
                dfs(rot.right, deep + 1)

        if depth==1:
            a=TreeNode(val)
            a.left=root
            return a
        else:
            dfs(root,1)
            return root


