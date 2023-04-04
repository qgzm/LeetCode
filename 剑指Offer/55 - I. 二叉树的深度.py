# 使用者：姜海波
# 创建时间：2023/4/4  11:43
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
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