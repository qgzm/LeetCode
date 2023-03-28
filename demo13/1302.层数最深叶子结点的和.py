# 使用者：姜海波
# 创建时间：2023/3/28  10:37
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxdepth=0
        ans=0
        def dfs(root:Optional[TreeNode],depth):
            if root is None:
                return
            nonlocal maxdepth,ans
            if depth>maxdepth:
                maxdepth=depth
                ans=root.val
            elif depth==maxdepth:
                ans+=root.val
            dfs(root.left,depth+1)
            dfs(root.right,depth+1)
        dfs(root,0)
        return ans
