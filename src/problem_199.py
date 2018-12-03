#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def rightSideView( root):
    """
    算法：层次遍历二叉树
    思路：
        本题思路比较直观，按层遍历二叉树，每一层的最后一个节点就是看到的结果
               1            <---
             /   \
            2     3         <---
             \     \
              5     4       <---
        ans = [1,3,4]
    复杂度分析：
        时间：ON，遍历所有节点
        空间：ON，递归栈的空间和ans的空间
    """
    if not root:
        return []
    curr_level = [root]
    ans = []
    while curr_level:
        ans.append(curr_level[-1].val)
        next_level = []
        for node in curr_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        curr_level = next_level
    return ans