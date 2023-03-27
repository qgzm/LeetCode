# 使用者：姜海波
# 创建时间：2023/3/27  12:23
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        que = collections.deque([root])
        ans = []
        flag = True
        while len(que) != 0:
            size = len(que)
            level = []
            for i in range(size):
                cur = que.popleft()
                level.append(cur.val)
                if cur.left is not None:
                    que.append(cur.left)
                if cur.right is not None:
                    que.append(cur.right)
            if not flag:
                level.reverse()
            ans.append(level)
            flag = not flag

        return ans



