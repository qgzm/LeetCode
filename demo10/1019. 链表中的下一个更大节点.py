# 使用者：姜海波
# 创建时间：2023/4/10  22:59
# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = list()
        s = list()

        cur = head
        idx = -1
        while cur:
            idx += 1
            ans.append(0)
            while s and s[-1][0] < cur.val:
                ans[s[-1][1]] = cur.val
                s.pop()
            s.append((cur.val, idx))
            cur = cur.next

        return ans



print(Solution().nextLargerNodes([2, 1, 5]))