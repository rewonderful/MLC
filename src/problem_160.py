#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from ListNode import ListNode


def getIntersectionNode_(headA, headB):
    """
    算法：
        当两个链表是相交的时候，如果链表等长那么p，q遍历时肯定有一时刻是相等的，问题在于一长一短的情况，当两个链表一长一短
        的时候，长链表指针比短链表多走lenA-lenB步，因此可以先求出两个链表的长度然后让长链表先走lenA-lenB步，然后二者在一起
        往后走，并且判断二者是否相等，相等的话则找到了两个链表的交点，返回相等处的节点，如果的确有交点，那么就会返回交点处的
        结点，否则的话，两个指针最后都到None了，因为None == None，所以最后返回的也是不想交情况下的正确答案
    复杂度分析：
        时间：ON，求链表长度O(m)，O（n），最后遍历相交O(m+n)
        空间：O1，指针及辅助变量不随输入规模变化而变化，是常数级
    """
    if headA == None or headB == None:
        return None
    lenA = 1
    hA = headA
    while hA.next != None:
        lenA += 1
        hA = hA.next

    lenB = 1
    hB = headB
    while hB.next != None:
        lenB += 1
        hB = hB.next
    hA = headA
    hB = headB
    if lenA > lenB:
        for i in range(lenA - lenB):
            hA = hA.next
    else:
        for i in range(lenB - lenA):
            hB = hB.next

    while hA != None and hB != None:
        if hA == hB:
            return hA
        hA = hA.next
        hB = hB.next
    return None

def getIntersectionNode__( headA, headB):
    """
    算法：
        较长的链表一定比较短的链表多走lenA-lenB步，那么当较长的链表如pA到达链表尾的时候，另其指向另一个链表头B并继续往下走，
        当pB也走到链表尾时，让它指向另一个链表头A并继续往下走，这样的话可以保障较短较长的pB多走m-n步，调换位置后接着一起往下走
        判断二者是否相等，如果有交点那么相等处一定是交点，否则二者都到链表尾为None，None == None，返回也是None，即无交点
    复杂度分析：
        时间：ON，求链表长度O(m)，O（n），最后遍历相交O(m+n)
        空间：O1，指针及辅助变量不随输入规模变化而变化，是常数级
    """
    if headA == None or headB == None:
        return None
    a = headA
    b = headB
    while a != b:
        a = headB if a == None else a.next
        b = headA if b == None else b.next
    return a
def getIntersectionNode(self, headA, headB):
    """
    算法："暴力"求解
        遍历headA，将headA中节点的内存地址存储起来，用哈希表速度快一点
        再遍历headB，判断其是否在record中第一个判断在的结点就是二者相交的公共结点
    复杂度分析：
        时间：On，遍历headA+遍历headB
        空间：On，遍历headA时存储headA的大小
    """
    record = {}
    if headA == None or headB == None:
        return None
    while headA != None:
        record[headA] = 1
        headA = headA.next
    while headB != None:
        if headB in record:
            return headB
        headB = headB.next
    return None


if __name__ == '__main__':
    headA = ListNode(3)
    headB = ListNode(2)
    headB.next = headA
    print(getIntersectionNode_(headA, headB))
