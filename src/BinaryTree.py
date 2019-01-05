#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from TreeNode import TreeNode
class BinaryTree(object):
    def __init__(self):
        self.root = None
    def get_test_tree(self):
        t1 = TreeNode(1)
        t2 = TreeNode(2)
        t3 = TreeNode(3)
        t4 = TreeNode(4)
        t5 = TreeNode(5)

        t1.left = t2
        t1.right = t3
        t3.left = t4
        t3.right = t5
        return t1
    def get_test_tree2(self):
        t1 = TreeNode(1)
        t2 = TreeNode(2)
        t3 = TreeNode(3)
        t4 = TreeNode(4)
        t5 = TreeNode(5)
        t6 = TreeNode(2)
        t7 = TreeNode(3)

        t5.left=t2
        t5.right = t3
        t3.left = t6
        t3.right = t4
        t6.left = t7
        t6.right = t1
        return t5

