# 使用者：姜海波
# 创建时间：2023/3/26  18:26
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while (cur.next != None):
            if cur.next.val==val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy_head.next

Solution().removeElements()
