#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        curr_level = [root]
        ans = []
        while (curr_level):
            val = [node.val for node in curr_level]
            ans.append(val)
            next_level = []
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                curr_level = next_level
        return ans

