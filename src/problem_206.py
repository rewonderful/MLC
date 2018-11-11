#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
def reverseList( head):
    """
    单链表逆置：
            设置一个哑节点，依次将原链表从头开始插入，新插入的节点p在哑节点后面，把哑节点的next接
            在新插入节点的后面，即实现了逆置
    时间复杂度： On，要遍历一次整个链表完成
    空间复杂度： O1 不论输入规模多大，只需要p，tmp这样的辅助变量即可完成
    """
    dummy = ListNode(0)
    p = head
    while p != None:
        tmp = p.next
        p.next = dummy.next
        dummy.next = p
        p = tmp
    return dummy.next
"""
    递归，思路是倒着来，先跑到最后一个节点，然后将最后一个节点变成p返回
    依次将前面head的next的next指向head
    注意将head.next置None，不然会形成环
    时间复杂度：On 递归n次
    空间复杂度：On 递归栈要用n个空间
"""

def reverseList_recur(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # 第一个head == None的判断是判断None的测试用例，这样写是二者结合了一下罢了：
    # if head ==None :return head
    # if head.next == None : return head
    if head == None or head.next == None:    
        return head
    p = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return p