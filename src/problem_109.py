#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from TreeNode import TreeNode
from ListNode import ListNode


def sortedListToBST( head):
    """
    My Method
    算法：递归+快慢指针找链表中点
    思路：
        整体思路和108题一样，就是选有序列表的中间点作为根节点来构建树
        关键在于如何找中间点
            用快慢指针的方法来找中间节点，可以参见第876题
            这里除了找中间点外，还要将整个游戏列表分为左右两个部分
            所以要找到mid的prev节点，然后【设置prev.next = None来断开与mid的联系】，进而转化为左右两个链表！
            这里我找prev的方法是设置一个prev节点,初始prev.next = head，这样就可以保证prev总是在slow的前一步
            或者另外一种方式见后面
        拿到中间点后以mid值建立节点，左侧就传head递归就好，此时head已经只剩[head,mid)部分了，右侧
        就传mid.next
            注意在上面还要判断一下当前节点是不是叶节点！如果是叶节点即mid == head，就不要往后传了直接 return root !
            否则会无限循环！[10]的mid是[10] --> [10]的mid是[10] --->....--> [10]的mid是[10]
    复杂度分析：
        时间：NlogN，solution中给的复杂度
        空间：OlogN，solution中给的复杂度
    """

    def getMidium(head):
        if not head:
            return None
        prev = ListNode(0)
        prev.next = head
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            prev = prev.next
        prev.next = None
        return slow

    def constructTree(head):
        if not head:
            return None
        medium = getMidium(head)
        root = TreeNode(medium.val)
        if head == medium:
            return root
        root.left = constructTree(head)
        root.right = constructTree(medium.next)
        return root

    return constructTree(head)
def sortedListToBST1( head):
    """
    Method Another

    这里主要是getMidium方法有变化
    先设prev = None
    在while中更新时，另prev = slow，prev等于slow未更新前的值，然后再更新slow，就可以达到获取slow的前一个节点的目的
    """

    def getMidium(head):
        if not head:
            return None
        prev = None
        prev.next = head
        fast = slow = head
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        if prev:
            prev.next = None
        return slow

    def constructTree(head):
        if not head:
            return None
        medium = getMidium(head)
        root = TreeNode(medium.val)
        if head == medium:
            return root
        root.left = constructTree(head)
        root.right = constructTree(medium.next)
        return root

    return constructTree(head)

def sortedListToBST2(self, head):
    """
    空间换时间
    将链表转化为数组然后再用108题的代码转化为BST
    转化时还可以用二分查找的方式来写，见sortedListToBST3
    """

    def linklist2list(head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr

    def sortedArrayToBST(nums):

        if nums == []:
            return None
        center = len(nums) // 2
        root = TreeNode(nums[center])
        root.left = sortedArrayToBST(nums[:center])
        root.right = sortedArrayToBST(nums[center + 1:])
        return root

    return sortedArrayToBST(linklist2list(head))

def sortedListToBST3(self, head):
    """
    这里用lo，hi指针来找中间节点来区分左右子区间
    其实是更为通用的！
        因为切片来取左右短点是Python独有的操作，如果用java，还是得用lo，hi指针来取，且取切片的复杂度为O(K)！
        K为切片序列长度
    复杂度分析：
        时间：ON，solution中给出的
        空间：ON，arr数组的大小

    """

    def mapListToValues(head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals

    values = mapListToValues(head)

    def convertListToBST(l, r):
        if l > r:
            return None
        mid = (l + r) // 2
        node = TreeNode(values[mid])
        if l == r:
            return node

        node.left = convertListToBST(l, mid - 1)
        node.right = convertListToBST(mid + 1, r)
        return node

    return convertListToBST(0, len(values) - 1)
def list2LinkedList(arr):
    if arr == []:
        return None
    head = ListNode(arr.pop(0))
    p = head
    while arr !=[]:
        p.next = ListNode(arr.pop(0))
        p = p.next
    return head
if __name__ == '__main__':
    head = list2LinkedList([-10,-3,0,5,9])
    print(sortedListToBST(head))
    pass


