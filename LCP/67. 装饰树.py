# 使用者：姜海波
# 创建时间：2023/6/3  14:28
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.left is not None:
            root.left = TreeNode(-1, self.expandBinaryTree(root.left), None)
            root.right = TreeNode(-1, None, self.expandBinaryTree(root.right))
        return root
