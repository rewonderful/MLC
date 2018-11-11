#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys
sys.path.append('./')
from ListNode import ListNode
def mergeTwoLists( l1, l2):
    """
    创建一个哑节点，逐个判断两个链表的元素，把较小的节点插入，最后由于可能两个链表不等长，
    将不为None的那个链表剩余部分插入即可
    时间复杂度:On 由l1,l2长度定
    空间复杂度：On dummy链表空间长度
    """
    dummy = ListNode(0)
    p = dummy
    while l1 != None and l2 != None:
        if l1.val <= l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    p.next = l1 if l1 != None else l2
    return dummy.next
"""
 递归:
    哪个node的值小，就返回哪个node，并且把这个node的next指针指向下一步比较，因为
    本节点已经返回了，所以下一次比较的时候应该是本节点的next和另外一个节点比较
    当一个节点为None的时候应该返回另外一个节点（就像一开始一个是None另外一个不是None一样返回另外一个）
    时间复杂度：On 递归n次
    空间复杂度：On 递归存储空间
   
"""
def mergeTwoLists_recur(self, l1, l2):

    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.val <= l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
    return l2