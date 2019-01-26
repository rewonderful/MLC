#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def connect(self, root):
    """

    Disscussion Method
        同样是按层遍历，不同的是，根据题目描述每一层都是完全二叉树，所以直接从root.left这样向下遍历就可以遍历完
    整颗树，每一层再看做是一种单链表的结构去遍历，
        如下面这个二叉树，拿到1，就可以用root.left和root.right来连接2和3了
        在连接第三层的时候，拿到2，连接4，5，然后用2.next.left来拿到6，进而将2.right和2.next.left连接在一起，这样
        2就可以挪到3，重复连接步骤了，即node=node.next
        然后外层循环的root控制现在处理的是哪一层，相当于外层的root记录的是每一层的头结点，
                    1 -> NULL
                   /  \
                  2 -> 3 -> NULL
                 / \  / \
                4->5->6->7 -> NULL
    """
    if root == None:
        return
    while root.left:
        node = root
        while node:
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            node = node.next
        root = root.left
def connect(self, root):
    """
    My Method
    很朴素地用层次遍历来连接节点，将节点塞入数组中后就可以逐个连接起来了，但是这样做时间复杂度和空间复杂度都相对较高
    """
    if root == None:
        return
    curr_level = [root]
    while curr_level:
        next_level = []
        for i in range(len(curr_level) - 1):
            curr_level[i].next = curr_level[i + 1]
        for node in curr_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        curr_level = next_level