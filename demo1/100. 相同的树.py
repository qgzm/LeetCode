# 使用者：姜海波
# 创建时间：2023/4/4  20:53
# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # dfs
        # if not p and not q:
        #     return True
        # elif not p or not q:
        #     return False
        # elif p.val != q.val:
        #     return False
        # else:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # bfs
        if not p and not q:
            return True
        if not p or q:
            return False
        queue1 = collections.deque([p])
        queue2 = collections.deque([p])
        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False
            if (not node1.left) ^ (not node2.left):
                return False
            if (not node1.right)^(not node2.right):
                return False
            if node1.left:
                queue1.append(node1.left)
            if node1.right:
                queue1.append(node1.right)
            if node2.left:
                queue2.append(node2.left)
            if node2.right:
                queue2.append(node2.right)
        return not queue1 and not queue2

