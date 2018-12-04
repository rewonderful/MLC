#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from TreeNode import TreeNode


def buildTree(self, inorder, postorder):
    """
    算法：递归
    思路：
        和105题用先序遍历序列和中序遍历序列解的方法相似，不同的是，
        1. 后序遍历，根节点是最后，所以直接pop()出栈
            而105题用先序遍历拿到的根节点，是pop(0)出队列，
        2.构建子树的时候，从右子树开始构建，因为后序遍历是"左-->右-->根"，当我从列表右侧pop()根节点
            出栈的时候，根节点近邻的是左侧的右子树，所以从右子树先开始构建，就可以保障用同全局的postorder
            向后递归传递，在右子树的节点都构造完后继续访问同一个postorder就可以拿到左子树的根节点了
    复杂度分析：
        时间：ON2，inorder.index寻找下标的操作要ON，嵌套递归ON，总ON2
        空间：ON，存储整个树节点，且递归栈也有空间
    """
    if inorder == []:
        return None
    root_val = postorder.pop()
    index = inorder.index(root_val)
    root = TreeNode(root_val)

    root.right = self.buildTree(inorder[index + 1:], postorder)
    root.left = self.buildTree(inorder[:index], postorder)
    return root

