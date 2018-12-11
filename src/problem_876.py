#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def middleNode(self, head):
    """
    很关键！
    用快慢指针求链表中点！
    快指针每次走2步，
    慢指针每次走1步
     2*t = s
     t = 1/2 s
     注意while循环的条件！
        fast首先不为None，且fast.next 也不为None，fast才可以一下走两步!要想清楚条件！不要就写上不管了
        如果条件只有fast != None,那么当链表为1时，fast会尝试从1往后跳两步！就错了！
        事实上
            要用fast != None and fast.next != None一个是很直观的因为fast=fast.next.next
            要用这个限制，再一个是因为链表的长度不是奇数，就是偶数，那么fast从当前位置开始一次跨越两步
            共经历了3个元素，间隔为2，所以链表长度为大于等于3的奇数时，可以直接跳到后面fast指向最后一个数，
            如12345中的5，如果是偶数，会扩充长度，走到最末端奇数位置的那个None，如1234None
            但是如果链表长度小于3，不加限制条件fast.next != None可能就会出问题！
            12，fast跳到12None的None
            但是1的话，fast应该不跳！
            所以好好品一品这里的while条件，不要再写错了！！！
    复杂度：
        时间：ON，遍历一遍节点
        空间：O1，常数级
    """
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow