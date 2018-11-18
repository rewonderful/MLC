#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class MinStack(object):
    """
    这里用一个最小栈来跟踪记录最小值的变化情况，主要是当操作为push的时候要判断一下
    如果push的值小于当前的最小值（最小栈栈顶值），直接将该元素push入栈，否则的话push当前栈顶，以此来保障最小栈
    跟踪了当前栈的最小值情况，保障这两个栈内元素数量是一样的并且是同步进行的push和pop操作
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_stack == []:
            self.min_stack.append(x)
        else:
            if x < self.min_stack[-1]:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack != []:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack != []:
            return self.min_stack[-1]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()