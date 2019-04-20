#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from ListNode import ListNode
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = head
        while p != None and p.next != None:
            if p.val == p.next.val:
                tmp = p.next.next
                p.next.next = None
                p.next = tmp
            else:
                p = p.next
        return dummy.next