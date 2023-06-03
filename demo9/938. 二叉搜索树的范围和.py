# 使用者：姜海波
# 创建时间：2023/6/3  14:55
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        if root.val>high:
            return self.rangeSumBST(root.left,low,high)
        elif root.val<low:
            return self.rangeSumBST(root.right,low,high)
        else:
            return root.val+self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high)
