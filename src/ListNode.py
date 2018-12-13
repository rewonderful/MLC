#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    def list2LinkedList(self,arr):
        if arr == []:
            return None
        head = ListNode(arr.pop(0))
        p = head
        while arr !=[]:
            p.next = ListNode(arr.pop(0))
            p = p.next
        return head