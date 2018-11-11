#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def detectCycle(self, head):
    """
    最笨的方法：
        将遍历过的节点存储起来，然后每次遍历的时候都判断当前节点有没有被遍历过，如果
        被遍历过（第一次遇到），那么就找到了环的开始部分
        如果最后有没有找到。说明链表没有环，应该返回None
    时间复杂度： On 至少要遍历到None或者环的开始处
    空间复杂度： On 辅助存储所有遍历过的节点
    """
    if head == None:
        return None
    record = []
    while head != None:
        if head in record:
            return head
        else:
            record.append(head)
        head = head.next
    return head

def detectCycle(self, head):
    """
    快慢指针法：
        设置快慢指针fast,slow，快指针一次2步，慢指针一次1步
        假设Head到环开始处距离为A，相遇点距离环开始处距离为B，则相遇时
        慢指针走了A+B，快指针走了2(A+B),
        相遇时快指针一定比慢指针多走一圈【
        可以推断出来，用假设法，如果超过一圈，则在之前肯定会相遇，所以一定是一圈】
        2(A+B) = A+B+N
        A+B=N,A=N-B
        所以当快慢指针相遇时，再设置另外的指针p，q一步一步走，二者相遇之处即走了距离A，即为环结点处
        时间复杂度： On 快指针循环次数和链表本身结构及链表长度有关（如无环，那么肯定是循环n的量级到None）
        空间复杂度： O1 fast,slow,p,q 4个辅助指针的空间大小，不随输入规模n变化
    """
    if head == None:
        return None
    fast = head
    slow = head
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            p = slow
            q = head
            while p != q:
                p = p.next
                q = q.next
            return p
    return None