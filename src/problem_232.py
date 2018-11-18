#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class MyQueue(object):
    """
    双栈法
        input_stack 用来处理push的数据
        output_stack 专门用来处理弹出和返回队列头的操作
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.input_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.output_stack == []:
            while self.input_stack != []:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.output_stack == []:
            while self.input_stack != []:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.input_stack == [] and self.output_stack == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        tmp = []
        for i in range(len(self.stack) - 1):
            tmp.append(self.stack.pop())
        peek = self.stack.pop()
        while tmp != []:
            self.stack.append(tmp.pop())
        return peek

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        tmp = []
        peek = None
        for i in range(len(self.stack)):
            peek = self.stack.pop()
            tmp.append(peek)
        while tmp != []:
            self.stack.append(tmp.pop())
        return peek

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack == []