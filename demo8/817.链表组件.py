# 使用者：姜海波
# 创建时间：2022/10/12  21:10
# Definition for singly-linked list.

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
满足两点之一:
结点的值在数组nums中且结点位于链表起始位置
结点的值在数组nums中且结点的前一个点不在数组中
它是组件的起始位置
'''


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        numsSet = set(nums)
        inSet = False
        res = 0

        while head:
            # head.val 不在nums里则赋值为假
            if head.val not in numsSet:
                inSet = False
            # 如果前面的val为假(此时已经判断出当前值在nums里),满足条件
            elif not inSet:
                inSet = True
                res += 1
            head = head.next
        return res
