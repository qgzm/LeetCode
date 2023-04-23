# 使用者：姜海波
# 创建时间：2023/4/18  21:22
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        ans = 0
        st = [(root, root.val, root.val)]
        # 维护每个结点祖先节点的最大值,最小值
        while st:
            node, mx, mn = st.pop()
            ans = max(ans, abs(node.val - mx), abs(node.val - mn))
            if node.right:
                st.append((node.right, max(node.right.val, mx), min(node.right.val, mn)))
            if node.left:
                st.append((node.left, max(node.left.val, mx), min(node.left.val, mn)))
        return ans
        """
        def dfs(root, mi, ma):
            if root == None:
                return 0
            diff=max(abs(root.val-mi),abs(root.val-ma))
            mi=min(mi,root.val)
            ma=max(ma,root.val)
            diff=max(diff,dfs(root.left,mi,ma))
            diff=max(diff,dfs(root.right,mi,ma))
            return diff
        return dfs(root,root.val,root.val)

