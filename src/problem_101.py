#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left and right:
            return (left.val == right.val) and self.isMirror(left.left, right.right) and self.isMirror(left.right,
                                                                                                       right.left)
        else:
            return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)