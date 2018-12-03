#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def chinese(data):
    """asdfadsfadsfsda"""
    count = 0
    for s in data:
        if ord(s) > 127:
            count += 1
    return count

def singleNumber( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            print(nums[i])
from TreeNode import TreeNode
def modify(t):

    b = t
    b.val = 3
    print('inner:',id(b))
if __name__ == '__main__':
    t = TreeNode(10)
    print(id(t))
    print(t.val)
    modify(t)
    print(id(t))
    print(t.val)





