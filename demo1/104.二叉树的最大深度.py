# 使用者：姜海波
# 创建时间：2023/3/27  12:36
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(root, depth):
            if root.left is None and root.right is None:
                return depth
            if root.left is not None and root.right is not None:
                return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
            if root.left is not None:
                return dfs(root.left, depth + 1)
            if root.right is not None:
                return dfs(root.right, depth + 1)

        return dfs(root, 1)