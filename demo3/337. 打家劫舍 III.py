# 使用者：姜海波
# 创建时间：2023/3/30  18:52
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def _rob(root: TreeNode):
            if not root:
                return 0, 0
            ls, ln = _rob(root.left)
            rs, rn = _rob(root.right)
            return root.val + ln + rn, max(ls, ln) + max(rs, rn)

        return max(_rob(root))