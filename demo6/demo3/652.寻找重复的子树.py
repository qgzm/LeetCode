# 使用者：姜海波
# 创建时间：2022/9/5  14:07

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional, List


# 哈希seen映射存储列到子树的映射
# 如果再计算序列时,通过seen查找到了已经出现过的序列,就可以吧对应的子树放到哈希集合repeat中,这样可以保证同一类的重复子树只会被存储一次
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            tri = (node.val, dfs(node.left), dfs(node.right))
            if tri in seen:
                (tree, index) = seen[tri]
                repeat.add(tree)
                return index
            else:
                nonlocal idx
                idx += 1
                seen[tri] = (node, idx)
                return idx

        idx = 0
        seen = dict()
        repeat = set()

        dfs(root)
        return list(repeat)
