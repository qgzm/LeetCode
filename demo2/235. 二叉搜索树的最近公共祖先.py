# 使用者：姜海波
# 创建时间：2023/6/9  16:34
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # ancestor = root
        # while True:
        #     if p.val < ancestor.val and q.val < ancestor.val:
        #         ancestor = ancestor.left
        #     elif p.val > ancestor.val and q.val > ancestor.val:
        #         ancestor = ancestor.right
        #     else:
        #         break
        # return ancestor
        def getpath(root: TreeNode, target: TreeNode):
            path = list()
            node = root
            while node != target:
                path.append(node)
                if target.val < node.val:
                    node = node.left
                else:
                    node = node.right
            path.append(node)
            return path

        path_p = getpath(root, p)
        path_q = getpath(root, q)
        for u, v in zip(path_p, path_q):
            if u == v:
                ancestor = u
            else:
                break
        return ancestor
