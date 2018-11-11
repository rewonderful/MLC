#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
快慢指针法
    1.快指针一次走2步，慢指针一次走1步，当快指针走到底时，慢指针刚好走到序列的一半
    2.慢指针变走边将过去的值存储起来，指针停下不走后，拿到中间节点half，然后一边遍历一边和前面存储起来的节点值比较
    时间复杂度：O（n）：On快慢指针走，On后半部分走
    空间复杂度O（n/2）：栈的空间

"""
def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head == None or head.next == None:
        return True
    fast = head
    slow = head
    stack = [head.val]
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
        stack.append(slow.val)
    half_right = slow.next
    if fast.next == None:
        stack.pop()
    while half_right != None:
        if half_right.val != stack[-1]:
            return False
        stack.pop()
        half_right = half_right.next
    return True
"""
    遍历链表，用list存储访问过的值，然后判断列表是否回文
    时间复杂度：On 遍历一次
    空间复杂度：On 建立辅助存储的列表空间
"""
 def isPalindrome(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        val = []
        while head != None:
            val.append(head.val)
            head = head.next
        return val == val[::-1]