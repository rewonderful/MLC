#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def __init__(self):
        self.sum = 0
    def convertBST(self, root):
        """
        算法：递归
        思路：
            中序遍历BST，并且从右子树开始，这样访问节点的顺序就是从大到小的！！
            [1,2,3,4,5,6,7],右➡️中➡️左访问：7654321
            那么在逆着访问的路上，依次把前序的值累加值sum记下来，并且当前节点值再加上sum就是要求的格式！
            ✨所以关键要看出来要逆着中序遍历就是倒着访问！！！！
        ❗️❗️❗️：
            一定要利用BST的特性！！！！
        复杂度分析：
            时间：ON，遍历一遍所有节点
            空间：ON，递归栈空间
        """
        if root == None:
            return None
        self.convertBST(root.right)
        root.val += self.sum
        self.sum = root.val
        self.convertBST(root.left)
        return root