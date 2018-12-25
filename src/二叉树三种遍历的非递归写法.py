#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def preorderTraversal(self, root):
    # 前序
    if root is None:
        return []
    stack = []
    seq = []  # 记录先序访问序列
    while ((root != None) | (len(stack) != 0)):
        if root != None:
            seq.append(root.val)  # 先访问根节点
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()  # 回溯至父节点
            root = root.right
    return seq

def inorderTraversal(self, root):
    # 中序
    if root is None:
        return []
    stack = []
    seq = []
    while ((root != None) | (len(stack) != 0)):
        if root != None:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            seq.append(root.val)  # 左孩子先pop出来，再pop根节点
            root = root.right
    return seq

def postorderTraversal(self, root):
    # 后序
    if root is None:
        return []
    stack = []
    seq = []
    output = []
    while ((root != None) | (len(stack) != 0)):
        if root != None:
            seq.append(root.val)
            stack.append(root)
            root = root.right  # 这从left变成了 right
        else:
            root = stack.pop()
            root = root.left  # 这从right变成了 left

    while seq:  # 后序遍历 是 将先序遍历的反过来
        output.append(seq.pop())
    return output


