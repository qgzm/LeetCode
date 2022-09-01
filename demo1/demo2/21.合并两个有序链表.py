# 使用者：姜海波
# 创建时间：2022/9/1  8:58
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 建立一个比所有数都小的结点
        prehead = ListNode(-1)
        # 新建数组的名字,并且赋值给第一个ListNode
        prev = prehead
        #判断两个链表都为空
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            #新链表也要跟着向下进一位
            prev = prev.next
        #最后有一个链表还有一个数,将其赋值进去
        prev.next = list1 if list1 is not None else list2
        #返回prev的第二个结点才为两个链表合并后的结果
        return prehead.next
