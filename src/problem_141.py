#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def hasCycle( head):
    """
    :type head: ListNode
    :rtype: bool

    """
    """
    1、设定两个指针：A、B，且开始时都指向头部

    2、A的遍历方式为：A=A.next，即一步一步走。B的遍历方式为：B=B.next.next，即一次走两步。

      有了以上两个方式，我们可以想如果有环那么B一定是可以追上A的。如果没有环那么B将最先走到最后。
    """
    if head == None:
        return False
    fast = head
    slow = head
    while fast != None:
        if fast.next != None:
            fast = fast.next.next
        else:
            return False
        slow = slow.next
        if fast == slow:
            return True
    return False

def hasCycle( head):
    """
    算法：
        哈希表存储访问过的结点，如果再次访问的时候结点已经在哈希表中了，则说明有环，且第一个发现已记录的结点就是环开始处
    复杂度分析：
        时间：On，和环的长度有关
        空间：On，和环的长度有关，辅助的哈希表大小
    """
    record = {}
    while head != None:
        if head in record:
            return True
        else:
            record[head] = 1
        head = head.next
    return False