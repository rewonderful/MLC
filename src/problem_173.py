#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class BSTIterator:
    """
    My Method Using Stack
    核心还是中序遍历，只不过这时候用栈来存储中间的状态
    其实首先看提议，要一直返回第ksmallest的，那就是要中序遍历
    并且某一时刻会有回溯的情况，肯定要用栈来保存的
    用栈来保存的话可以使得存储空间降低到Oh
    hasNext可以是O1，但是next并不能是O1
    """

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.appendLeft(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        curr = self.stack.pop()
        self.appendLeft(curr.right)
        return curr.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) != 0

    def appendLeft(self, node):
        while node != None:
            self.stack.append(node)
            node = node.left
class BSTIterator1:
    """
    My Brute Froce Method
    中序遍历存起来在queue中，然后next就相当于是queue.pop
    hasNext就看队列是否为空
    这样能保障next和hasNext是O1，但是整体存储是ON，直接存下来所有的节点值了
    """
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.queue = []

        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            self.queue.append(root.val)
            inorder(root.right)

        inorder(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.queue.pop(0)

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.queue) != 0