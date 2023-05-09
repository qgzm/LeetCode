# 使用者：姜海波
# 创建时间：2023/5/9  19:03
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # def dfs(root:Optional[TreeNode], floor:int):
        #     if floor>
        deq = collections.deque()
        deq.append(root)
        while deq:
            root = deq.popleft()
            if not root.right:000000000
                deq.append(root.right)
            if not root.left:
                deq.append(root.left)

        return root.val
