#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    """
    叶子节点高度是1，所以None节点高度是0
    上层节点就是左右子树高度最大的+1即可
    """
    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1