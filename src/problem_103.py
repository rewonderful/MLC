#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    """
    比较naive的想法，正常的层次遍历，然后根据奇数层还是偶数层，翻转一下值的顺序
    """

    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        ans = []
        queue = [root]
        direction = 0
        while queue:
            vals = []
            next_level = []
            while queue:
                node = queue.pop(0)
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if len(ans) % 2 != 0:
                ans.append(vals[::-1])
            else:
                ans.append(vals)
            queue = next_level

        return ans

def zigzagLevelOrder( root) :
    """
    :param root:
    :return:
    比较优美的代码方式，通过前序遍历来遍历整棵树
    每一层遍历的时候根据树的深度来为res append新的存结果的空间
    根据当前层的奇数偶数来决定是正的插还是倒的插
    因为是 根->左->右 的顺序，所以左节点会先插进去，那么如果按照正常的层次遍历的话，就直接都append就可以了
    但是这里要求zigzag，那么就根据奇数层和偶数层，首先第一层的0层，可以看到，偶数层是尾部添加，正着来的，奇数层是
    首部添加，insert插进去的，并且因为是前序遍历，根左右，所以倒着插的话自然就是跟右左了，符合zigzag

    可以用这种代码去试试层次化访问二叉树！
    """
    def preorder(root, level, res):
        if root:
            if len(res) < level + 1: res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level] = [root.val] + res[level]
            preorder(root.left, level + 1, res)
            preorder(root.right, level + 1, res)

    res = []
    preorder(root, 0, res)
    return res

