# 使用者：姜海波
# 创建时间：2023/6/6  19:35
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 1
            lef=dfs(root.left)
            righ=dfs(root.right)
            return max(lef,righ)+1
        dfs(root)
