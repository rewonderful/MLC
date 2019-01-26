#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def sumNumbers(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.sum = 0

    def dfs(root, path):
        if root == None:
            return
        path *= 10
        path += root.val
        if not root.left and not root.right:
            self.sum += path
        dfs(root.left, path)
        dfs(root.right, path)

    dfs(root, 0)
    return self.sum
