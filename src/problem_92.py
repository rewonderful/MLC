#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from ListNode import ListNode

def reverseBetween( head, m, n):
    """
    问题分析：
        1. 设置一个哑节点把原列表的元素一个一个插进来，并且哑节点的存在可以处理m=1时的情况
        2. 逆置方法和普通链表逆置类似，但是要注意插入的不同，单纯逆置整个链表直接设置一个dummy头结点就好，此题要将小于m前的那个元素设为"头"节点
        3. 在小于m前，就普通的把节点正常接在后面，当进入[m,n]的区间后，就应该用逆置的方法倒着一个一个插入
        当到了n之后，就把链表的剩余部分接入已经连接起来的部分就好了
    算法：
        同上
    复杂度分析：
        时间：On，对链表循环一次就够了
        空间：On，返回的新链表需要On的空间
    """
    if m >= n:
        return head
    dummy = ListNode(0)
    p = head
    q = dummy
    counter = 1
    while counter <= n:
        if counter == m:
            sub_head = q
            q = p
        if m <= counter:
            tmp = sub_head.next
            sub_head.next = p
            pnext = p.next

            p.next = tmp
            p = pnext
        else:
            q.next = p
            p = p.next
            q = q.next
        counter += 1
    q.next = p
    return dummy.next