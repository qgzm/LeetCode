# 使用者：姜海波
# 创建时间：2023/3/7  23:52
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def construct_paths(root,path):
            if root:
                path+=str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path+="->"
                    construct_paths(root.left,path)
                    construct_paths(root.right,path)
        paths=[]
        construct_paths(root,'')
        return paths
