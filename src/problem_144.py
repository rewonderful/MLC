#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def preorderTraversal(self, root):
    """
    先序遍历：递归版
    """
    ans = []

    def travel(root):
        if root == None:
            return
        ans.append(root.val)
        travel(root.left)
        travel(root.right)

    travel(root)
    return ans

def preorderTraversal1(self, root):
    """
    非递归版：
        设置一个栈保存将要访问的节点

        stack pop 先访问root.val
        root的左右孩子，因为先序的顺序是根左右，所以入栈顺序是先右后左
        如果右孩子不空，压入
        如果左孩子不空，压入
    """
    if root == None:
        return []
    stack = [root]
    ans = []
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
    return ans