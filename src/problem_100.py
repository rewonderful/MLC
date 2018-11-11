#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p and q:
        left = isSameTree(p.left, q.left)
        right = isSameTree(p.right, q.right)
        return (p.val == q.val) and left and right
    else:
        return not p and not q