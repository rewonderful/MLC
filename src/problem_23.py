#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from ListNode import ListNode
from Queue import PriorityQueue

def mergeKLists(self, lists):
    """
    算法：优先队列法
        比较lists中的链表头节点的值，取值最小的node出来，将其插入到结果链表中，然后该链表替换为它的next，如果next是None就不添加，
        重复这个步骤直至lists中所有链表都空
        使用优先队列来完成pop最小值的过程，其实就是建立了一个最小堆，每次弹出堆顶，然后新进元素进入队列
    复杂度分析：
        时间：Onlogk，k是链表数量，pop用O1，插入元素要logk，构建n个元素的链表要用On的时间
        空间：-----，On构建n个元素的链表，优先队列占用Ok
    """
    dummy = p = ListNode(0)
    q = PriorityQueue()
    for node in lists:
        if node != None:
            q.put((node.val, node))
    while not q.empty():
        x, node = q.get()
        p.next = ListNode(x)
        p = p.next
        next_node = node.next
        if next_node != None:
            q.put((next_node.val, next_node))
    return dummy.next
def mergeKLists(self, lists):
    """
    算法：归并排序（分治思想）-由底向上的，两两合并直至剩下最后一个
        将原问题分解为更小更容易解决的子问题，将子问题合并后就得到原问题的解
        以下这个是非递归的解法，interval是每次合并取的间隔，每interval个链表进行合并
        因为是两两合并，所以合并后下一次interval要*=2，需要分治的两两子元素间相邻interval
        这里合并后还赋给了list[i]，就不需要额外申请空间存储合并后的链表，相当于将合并的结果最终都存在了第0个元素中
    复杂度分析：
        时间：Onlogk ，n是结点总数，归并需要nlogk的时间，k是链表数量，合并两个链表要On，故总Onlogk
        空间：O1，在原链表上操作，辅助空间常数级
    """
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else lists


def mergeTwoLists_merge_recursion(self, l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.val <= l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2


def mergeKLists(self, lists):
    """
    算法：归并排序（分治思想）-由顶向下的，将原问题分解为更小的子问题然后逐个解决子问题后合并
        递归，将原列表递归地分成左右两个子列表left，right进行处理，对left和right做merget操作，最后返回的就是排序后的链表
    复杂度分析：
        时间：Onlogk，k是链表数量，合并两个链表要On，故总Onlogk
        空间： Ologn，对n个元素，要递归调用logn次，递归栈占用空间logn
    """
    if lists == []:
        return None
    if len(lists) == 1:
        return lists[0]
    left = self.mergeKLists(lists[:len(lists) // 2])
    right = self.mergeKLists(lists[len(lists) // 2:])
    head = self.mergeTwoLists(left, right)
    return head


def mergeKLists_merge_no_recursion(self, lists):
    """
    算法：归并排序（分治思想）-由底向上的，
        自己写的，通俗易懂。两两合并直至剩下最后一个
    复杂度分析：
        时间：Onlogk，k是链表数量，合并两个链表要On，故总Onlogk
        空间：Onlogk(不一定对)，对k个链表，循环调用logk次，combine新建k次，combine长度On，总Onlogk
    """

    def mergeTwoLists(l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            l1.next = mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = mergeTwoLists(l1, l2.next)
            return l2

    if lists == []:
        return None
    if len(lists) == 1:
        return lists[0]
    while len(lists) > 1:
        combine = []
        for i in range(0, len(lists), 2):
            if i + 1 <= len(lists) - 1:
                combine.append(mergeTwoLists(lists[i], lists[i + 1]))
            else:
                combine.append(mergeTwoLists(lists[i], None))
        lists = combine
    return lists[0]
def mergeKLists_bruteforce(self, lists):
    """
    算法："暴力"求解
        遍历链表，将所有元素添加进一个list，对list排序后构建成链表的形式
    复杂度分析：
        时间：Onlogn，转为list要On，排序Onlogn，转成链表On，共Onlogn
        空间：On，sort的空间+最后新建后返回的On长度的链表
    """
    nodes = []
    for i in range(len(lists)):
        head = lists[i]
        while head != None:
            nodes.append(head.val)
            head = head.next
    nodes.sort()
    dummy = ListNode(0)
    p = dummy
    for x in nodes:
        p.next = ListNode(x)
        p = p.next
    return dummy.next