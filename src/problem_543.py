#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def diameterOfBinaryTree(self, root):
    """
    一个节点要么作为路径的一部分，要么就是作为路径的根节点
    作为路径的根节点时，路径长就是左孩子的最大高度+右孩子的最大高度+1
    所以用计算高度的方式来计算，更新self.ans
    return的时候return当前高度，也就是说自己作为路径的一部分时的情况，

    这个题有点像124题
    """
    self.ans = 1

    def getHeight(root):
        if root == None:
            return 0
        l = getHeight(root.left)
        r = getHeight(root.right)
        self.ans = max(self.ans, l + r + 1)
        return max(l, r) + 1

    getHeight(root)
    return self.ans - 1