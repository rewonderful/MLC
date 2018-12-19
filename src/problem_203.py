#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from ListNode import ListNode
def removeElements(self, head, val):
    """
    算法：dummy节点
    思路：
        设置dummy节点，head节点向后遍历，如果找到==val的head就删除，否则的话指针向后挪
    复杂度分析：
        时间：ON
        空间：O1
    """
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy

    while head:
        if head.val == val:
            pre.next = head.next
            head = pre.next
        else:
            head = head.next
            pre = pre.next
    return dummy.next