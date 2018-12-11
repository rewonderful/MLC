#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def invertTree(self, root):
    """
    算法：递归
    思路：
        递归将左子树和右子树调换
    复杂度分析：
        时间：ON，遍历所有节点
        空间：ON，递归栈空间
    """
    if root == None:
        return None
    left = self.invertTree(root.left)
    right = self.invertTree(root.right)
    root.left = right
    root.right = left
    return root

def invertTree(self, root):
    """
    算法：非递归方式
    思路：
        层次遍历的方式
    复杂度分析：
        时间：ON，遍历所有节点
        空间：ON，队列的空间
    """
    if root == None:
        return None
    queue = [root]
    while queue != []:
        node = queue.pop(0)
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return root