# @Time : 2024/7/23 21:40
# @Author : 姜海波
# @Version：V 0.1
# @File : 141. 环形链表.py
# @desc :
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
