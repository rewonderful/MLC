#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from ListNode import ListNode
def swapPairs(self, head):
    """
    My Method
    算法：倒插
    思路：
        本题思路比较直观，就是新建一个dummy，然后给原链表也建一个头节点，每两个结点倒插
        到新的dummy后，如果出现落单的那直接在尾部插入其即可，说明一定是最后一个结点了，
        9=2*4+1，8=2*4
        要注意的是每次倒插完之后要将p.next 置None，断掉尾部节点与原链表之间的关系
    复杂度分析：
        时间：ON，遍历一遍链表
        空间：O1，常数级
    """
    if head == None or head.next == None:
        return head
    dummy = ListNode(0)
    p = dummy
    dummy_head = ListNode(0)
    dummy_head.next = head

    while dummy_head.next != None:
        if dummy_head.next.next != None:
            p.next = dummy_head.next.next
            tmp = dummy_head.next
            dummy_head.next = dummy_head.next.next.next
            p = p.next
            p.next = tmp
        else:
            p.next = dummy_head.next
            dummy_head.next = None
        p = p.next
        p.next = None
    return dummy.next