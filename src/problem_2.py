#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import copy
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 == None:
        return l2
    if l2 ==None:
        return l1
    p1 = l1
    p2 = l2
    ans = ListNode(0)
    while p1 != None:
        if p2 != None:
            node_val = p1.val + p2.val
            if node_val >= 10:
                node_val =  node_val-10
                if p1.next!=None:
                    p1.next.val += 1
                else:
                    p1.next = ListNode(1)
            p1.val = node_val
            p2 = p2.next
        else:
            if p1.val >=10:
                p1.val = p1.val-10
                if p1.next !=None:
                    p1.next.val +=1
                else:
                    p1.next = ListNode(1)
        if p1.next == None:
            break
        else:
            p1 = p1.next

    if p2 != None:#(p1 == None,and p2!= none)
        p1.next = p2
    return l1






def delNode(l1,num):
    p = l1
    while p != None:
        if p.next != None and p.next.val == num:
            p.next = p.next.next
            print(p.next.val)
        p = p.next
    return l1





if __name__ == '__main__':
    #243 564
    l1 = ListNode(0)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(1)



    l2 = ListNode(7)
    l2.next = ListNode(3)
    # l2.next.next = ListNode(4)

    addTwoNumbers(l1,l2)

