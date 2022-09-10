# 使用者：姜海波
# 创建时间：2022/9/10  10:48
from idlelib.tree import TreeNode
from typing import Optional

'''对根结点root 进行深度优先遍历。对于当前访问的结点，如果结点为空结点，直接返回空结点；
如果结点的值小于 low，那么说明该结点及它的左子树都不符合要求，我们返回对它的右结点进行修剪后的结果；
如果结点的值大于high，那么说明该结点及它的右子树都不符合要求，我们返回对它的左子树进行修剪后的结果；
如果结点的值位于区间 [{low}, {high}][low,high]，我们将结点的左结点设为对它的左子树修剪后的结果，右结点设为对它的右子树进行修剪后的结果。

'''
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
