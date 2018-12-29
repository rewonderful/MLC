#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from ListNode import ListNode
def sortList(self, head):
    """
    暴力解法，将node都取出来然后重新拼接
    """
    nodes = []
    while head != None:
        nodes.append(head)
        the_next = head.next
        head.next = None
        head = the_next
    nodes.sort(key=lambda x: x.val)
    dummy = ListNode(0)
    p = dummy
    for node in nodes:
        p.next = node
        p = p.next
    return dummy.next

def sortList1( head):
    """
    My MergeSortMethod
    算法：归并排序
    思路：
        分而治之
        将链表划分为左右两个部分，然后对左右两个部分不停地划分直到剩下单个元素，就好排序了，排完后进行合并，
        也就是有序链表合并，就可以完成排序了

        要注意mid_pre
            用快慢指针走的话，slow的位置将是1，而归并要一分为二，mid应该在2那个位置，所以用mid_pre滞后记录slow的前一个位置，
        是要分割用的mid位置
        链表：4-->2-->1-->3-->None，
                     ^         ^
                     |         |
                    slow      fast
    复杂度分析：
        时间：NLOGN
        空间：O1，不考虑递归栈的话
    """

    def merge_sort(left, right):
        if left == None:
            return right
        if right == None:
            return left
        dummy = ListNode(0)
        p = dummy
        while left and right:
            if left.val <= right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        if left != None:
            p.next = left
        if right != None:
            p.next = right
        return dummy.next

    def merge(head):
        if head == None or head.next == None:
            return head
        fast = slow = head
        mid_pre = None
        while fast and fast.next:
            mid_pre = slow
            slow = slow.next
            fast = fast.next.next

        right_head = mid_pre.next
        mid_pre.next = None
        left = merge(head)
        right = merge(right_head)

        return merge_sort(left, right)

    return merge(head)

def sortList2(self, head):
    """
    Disscussion QuickSort
    算法：快排
    思路：
        快排的链表写法，要注意一些dummy节点的运用，以及记录pre和post等
    复杂度分析：
        时间：NLOGN
        空间：01，不考虑递归栈的话
    """

    def partition(start, end):
        node = start.next.next
        pivotPrev = start.next
        pivotPrev.next = end
        pivotPost = pivotPrev
        while node != end:
            temp = node.next
            if node.val > pivotPrev.val:
                node.next = pivotPost.next
                pivotPost.next = node
            elif node.val < pivotPrev.val:
                node.next = start.next
                start.next = node
            else:
                node.next = pivotPost.next
                pivotPost.next = node
                pivotPost = pivotPost.next
            node = temp
        return [pivotPrev, pivotPost]

    def quicksort(start, end):
        if start.next != end:
            prev, post = partition(start, end)
            quicksort(start, prev)
            quicksort(post, end)

    newHead = ListNode(0)
    newHead.next = head
    quicksort(newHead, None)
    return newHead.next
if __name__ == '__main__':
    head = ListNode(4)
    l1 = ListNode(2)
    l2 = ListNode(1)
    l3 = ListNode(3)
    head.next = l1
    l1.next = l2
    l2.next = l3



    print(sortList1(head))
