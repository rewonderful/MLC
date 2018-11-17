#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from ListNode import ListNode


def partition( head, x):
    """
    算法：
        设置两个哑结点，遍历链表，依次判断结点值和x的大小，小于x的插到left中，大于x的插到right中，直到整个链表遍历完
        ！！！注意最后q.next=None，断掉和后续的连接，否则会产生环，q是大于的那一侧，最后一个Q一定是最后结果的最后一个节点，所以可以安心
             另q.next = None
    复杂度分析：
        时间：On，遍历原链表需要On
        空间：O1，left 和 right 两个辅助头结点，后面接起来left和right也是把原链表接过来，并没有创建新的空间
    """
    left = ListNode(0)
    p = left
    right = ListNode(0)
    q = right

    while head != None:
        if head.val < x:
            p.next = head
            p = p.next
        else:
            q.next = head
            q = q.next
        head = head.next
    q.next = None  #!!!注意这里
    p.next = right.next
    return left.next

def partition_(self, head, x):
    """
    算法：与上述方法相似，不同的是这里每次创建新的节点，这样最后就不用q.next = None了，但是这样会增大空间复杂度
        时间：ON，遍历原链表需要On
        空间：ON，两个辅助链表需要ON+ON，故总ON
    """
    left = ListNode(0)
    p = left
    right = ListNode(0)
    q = right

    while head != None:
        if head.val < x:
            p.next = ListNode(head.val)
            p = p.next
        else:
            q.next = ListNode(head.val)
            q = q.next
        head = head.next
    p.next = right.next
    return left.next
if __name__ == '__main__':
    #[1,4,3,2,5,2]
    head = ListNode(1)
    n1 = ListNode(4)
    n2 = ListNode(3)
    n3 = ListNode(2)
    n4 = ListNode(5)
    n5 = ListNode(2)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    print(partition(head,3))
    p = partition(head,3)
    while p != None:
        print(p.val)
        p = p.next