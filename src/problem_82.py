#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
"""
1.由于链表的第一个元素可能就是重复的，所以要创建一个哑头结点来串起来整个链表
2.设置两个指针，一个指向当前正在遍历的节点curr，另外一个指向"前驱节点"pre，最后整个链表的形式就应该是前驱把后面的一个一个节点都串联起来，
  其实curr的指针一定会遍历完整个链表（所以基本结构会有while(curr != None): curr = curr.next），关键在于何时让前驱指针的next指向该指
  向的下一个节点 
3.由于链表的第一个元素可能就是重复的，所以curr初始化后要先用while向后移动，移动到curr.val != curr.next.val时，判断pre.next的关系
"""
def deleteDuplicates( head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None:
        return None
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    curr = head
    while curr != None:
        while curr.next != None and curr.val == curr.next.val: #由于链表的第一个元素可能就是重复的，所以curr初始化后要先用while向后移动，
            curr = curr.next
        #此时此刻的 curr 一定和curr.next是不等的
        #那么如果pre的next就是curr的话，pre就可以后移了(毕竟一开始的时候，curr = head，pre = dummy，他俩就是一前一后的关系)，
        if pre.next == curr:  #这里也可以视为是判断原链表第一个元素就有重复元素情况下做的判断，此时已经可以保证pre的next与pre.next.next也是不等的
            pre = curr
        #如果pre的next不是curr，说明curr在前面循环的时候发生了挪动，但是挪动后的curr在这依旧满足curr!= curr.next，
        # 所以pre的next 应该接curr的next
        else:
            pre.next = curr.next
        curr = curr.next
    return dummy.next

def deleteDuplicates1(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    p定位不重复元素的位置，q在重复区间一直查找
    """
    if head == None or head.next == None:
        return head
    dummy = ListNode(0)
    dummy.next = head
    p = dummy
    while p:
        q = p.next
        if q and q.next and q.val == q.next.val:
            while q != None and q.val == p.next.val:
                q = q.next
            p.next = q
        else:
            p = p.next
    return dummy.next