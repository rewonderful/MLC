#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return 0
    if root.left == None:
        return self.minDepth(root.right) + 1
    if root.right == None:
        return self.minDepth(root.left) + 1
    return min(self.minDepth(root.right), self.minDepth(root.left)) + 1