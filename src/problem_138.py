#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from RandomListNode import RandomListNode


class Solution(object):
    def __init__(self):
        self.visited = {}
    def copyRandomList__(self, head):
        """
        算法：
            将新链表的每个节点依次插在旧链表的每个节点后面，这样就可以保持原链表和新链表的关系，不会割裂开来
            【割裂】开来意味着譬如我自己想到的哈希表做法，只能用哈希表对新旧节点进行映射，而将原链表与新链表连接起来的做法就
            可以保持原节点与新节点之间的关系（原链表节点p_old.next就是新链表的节点），而不需要额外ON的辅助空间
            故可将问题分解为如下步骤：
                1. 遍历原链表copy每个节点并且插在原链表对应每个节点的节点后
                2. 将原链表每个节点的random指针指向结果copy给新链表的节点，p.next.random = p.random.next,注意p = p.next.next
                3. 将新链表从原链表中拆分下来，返回copy的新链表
        复杂度分析：
            时间: ON，多次循环都需要遍历整个链表
            空间: O1，辅助指针空间，常数级
        """
        if head == None:
            return None
        p = head
        while p != None:
            copy = RandomListNode(p.label)
            copy.next = p.next
            p.next = copy
            p = copy.next
        p = head
        while p != None:
            if p.next != None and p.random != None:
                p.next.random = p.random.next
            p = p.next.next

        p_old = head
        p_new = head.next
        head_new = head.next
        while p_old != None:
            p_old.next = p_old.next.next if p_old.next != None else None
            p_new.next = p_new.next.next if p_new.next != None else None
            p_old = p_old.next
            p_new = p_new.next
        return head_new
    def getClonedNode(self, node):
        if node != None:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = RandomListNode(node.label)
                return self.visited[node]
        return None
    def copyRandomList_(self, head):
        """
        算法：
            遍历原链表，对每个节点逐个进行复制，next指针就复制next指针，random指针就复制random指针
            注意这里由于节点间可能形成环，所以要用一个visited哈希表来记录访问过得节点，体现在getCloneNode中
            如果节点已经访问过，那么再次访问的时候直接返回visited[old_node]映射的新copy节点即可，否则的话说明
            该节点没有访问过，新建一个节点和old_node值相同，next和random为空
                1. 在"主函数"中，从头开始遍历，对每个节点进行复制，头节点是第一个首次visit的节点，将其加入visted中
                2. 遍历新copy的链表，对每个节点的next和random从原链表old_node用getCloneNode获取其next和random的copy节点
                3. 返回新链表的头结点
        复杂度分析：
            时间：ON，对原链表遍历一次
            空间：ON，对整个原链表的哈希值记录visited消耗ON
        """
        if head == None:
            return None
        old_node = head
        new_node = RandomListNode(head.label)
        self.visited[old_node] = new_node

        while old_node != None:
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            new_node = new_node.next
            old_node = old_node.next
        return self.visited[head]

    def copyRandomList(self, head):
        """
        算法：递归
            由于原链表中的random可以指向任意一个节点或None，可以将原链表节点抽象为图的结构，若无环的话则可以想象成
            是一颗树的结构，复制一颗树的话，就可以用到递归的思想，尤其本题的random和next刚好两个指针，相当于二叉树
            中的left和right，因此可以用递归的方法去copy节点
                将copy.next = 递归(old.next)，copy.random = 递归(old.random)
            但是要注意由于有环的存在，所以也要建立一个哈希表来完成visit记录，若某节点已经在visit中了则直接返回vist[old]，
            否则在vist中添加该项，vist[old] = copy，这样便可以避免图中的环造成的死循环

        复杂度分析：
            时间：ON，递归N次，N个节点
            空间：ON，递归栈的空间和哈希表的空间，合起来也是ON
        """
        if head == None:
            return None
        if head in self.visited:
            return self.visited[head]
        node = RandomListNode(head.label)
        self.visited[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

    def copyRandomList_mine(self, head):
        """
        算法：
            遍历原链表，next指针就正常的接下去，对random指针做额外的处理，即用哈希表映射，一个是记录原链表中每个节点的random是
            原链表中的哪个节点，一个是将原链表的内存地址与新链表的内存地址进行映射，如此一来算法共两大部分
                1. 遍历原链表，建立新链表，本次遍历建立next指针的关系，并且记录原链表random指针与新旧node的地址映射关系
                2. 遍历新链表，查询哈希表，得到当前新节点在原节点中对应的random的地址old_random并且用哈希表得到old_random对应
                的新节点new_radnom的位置，然后设置当前新节点p的random指针p.random = new_random
        复杂度分析：
            时间：ON，遍历两次链表，合计ON
            空间：ON，辅助指针及两个哈希表的存储空间，合计ON
        """
        node2random = {}
        node2node = {}
        dummy = RandomListNode(0)
        p = dummy
        while head != None:
            p.next = RandomListNode(head.label)
            p = p.next

            node2random[p] = head.random
            node2node[head] = p

            head = head.next
        p = dummy.next
        while p != None:
            if node2random[p] != None:
                p.random = node2node[node2random[p]]
            p = p.next
        return dummy.next