#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#https://www.cnblogs.com/xiaolovewei/p/7763867.html
class BinaryTree:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def DFS_recursion(tree):
    if not tree:
        return
    print(tree.val)
    DFS_recursion(tree.left)
    DFS_recursion(tree.right)
def DFS(root):
    if not root:
        return
    stack = [root]
    while(stack):
        top = stack.pop()
        print(top.val)
        if top.right is not None:
            stack.append(top.right)
        if  top.left is not None:
            stack.append(top.left)
def DFS_count(root):
    if not root:
        return 0
    stack = [root]
    max_depth = 1
    while(stack):
        top = stack.pop()
        print(top.val)
        if top.right is not None:
            stack.append(top.right)
        if  top.left is not None:
            stack.append(top.left)
if __name__ == '__main__':
    root = BinaryTree(1)
    root.left=BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left=BinaryTree(4)
    root.left.right=BinaryTree(5)
    root.left.left.left = BinaryTree(55)
    root.right.left=BinaryTree(6)
    root.right.right=BinaryTree(7)

    DFS(root)
