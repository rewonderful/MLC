#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
def removeNthFromEnd( head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    我的思路：
        建立哈希表，其实相当于数组,将每个节点的地址存起来，然后根据下标就可以判断从删除元素的位置，
        用空间换时间
    """
    if head == None or head.next == None:
        return None
    pointer_dict = {}
    counter = 1
    p = head
    # pointer_dict[0] = p.next
    while (p != None):
        pointer_dict[counter] = p
        counter += 1
        p = p.next
    pointer_dict[counter] = None

    former_index = len(pointer_dict) - n - 1
    after_index = len(pointer_dict) - n + 1
    if former_index == 0:
        return pointer_dict[2]
    pointer_dict[former_index].next = pointer_dict[after_index]
    return head
def removeNthFromEnd2( head, n):
    """
    :param head:
    :param n:
    :return:
    快慢指针，要删除的节点的前驱节点和最后一个节点之间的距离是固定的，利用这个特性，可以设置一个快慢指针，快指针先行N步，慢指针再走
    含头结点的做法如下:
    """
    if head == None or head.next == None:
        return None
    dummy = ListNode(0)
    dummy.next = head
    fast = dummy
    slow = dummy
    counter = 0
    while fast.next != None:
        if counter >= n:
            slow = slow.next
        fast = fast.next
        counter += 1
    if slow == dummy:
        return head.next
    else:
        slow.next = slow.next.next
        return head


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    同设置快慢指针，快指针先行n步，做判断，然后慢指针再开始走
    不含头结点:
    """
    fast = head
    slow = head
    counter = 0
    for _ in range(n):
        fast = fast.next
    if fast == None:
        return head.next

    while fast.next != None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
