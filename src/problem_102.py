#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import TreeNode
def levelOrder( root):
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
if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n1.left = n2
    n1.right = n5
    n2.left = n3
    n2.right = n4
    n5.right = n6
    print(levelOrder(n1))

