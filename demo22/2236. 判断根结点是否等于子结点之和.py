# 使用者：姜海波
# 创建时间：2023/4/27  22:22
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # def dfs(root:Optional[TreeNode]):
        #     if root.left is not None and root.right is not None:
        #         if root.left.val+root.right.val!=root.val:
        #             return False
        #         return dfs(root.left) and dfs(root.right)
        #     else:
        #         return
        return root.left.val + root.right.val == root.val
