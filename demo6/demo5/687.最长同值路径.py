# 使用者：姜海波
# 创建时间：2022/9/2  16:27
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # def panduanl(i):
        #     if i.val == i.left.val:
        #         return 1+panduanl(i.left)+panduanr(i.right)
        #     else:
        #         return 0
        # def panduanr(i) :
        #     if i.val == i.right.val:
        #         return 1+panduanl(i.left)+panduanr(i.right)
        #     else:
        #         return 0
        # p=[]
        # for i in root:
        #     j=1
        #
        #     j+=panduan(i)
        # return j

        ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left1 = left + 1 if node.left and node.left.val == node.val else 0
            right1 = right + 1 if node.right and node.right.val == node.val else 0
            nonlocal ans
            ans = max(ans, left1 + right1)
            return max(left1, right1)

        dfs(root)
        return ans
