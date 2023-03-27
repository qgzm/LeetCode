# 使用者：姜海波
# 创建时间：2023/3/27  15:08
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = None
        p = head
        while p is not None:
            nex = p.next
            p.next = end
            end = p
            p = nex
        return end
