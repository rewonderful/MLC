#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        top = None
        for i in range(len(self.queue)):
            top = self.queue.pop(0)
            self.queue.append(top)
        return top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue == []