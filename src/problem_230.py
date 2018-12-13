#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def kthSmallest(self, root, k):
    """
    My Method 1
    算法：暴力
    思路：
        BST的特征是有序，中序遍历BST就可以得到一个有序序列，那么这个有序序列的第k个位置的数就是答案
        所以中序遍历BST，并且将遍历的节点值append 到数组，数组长度等于k时达到要求，return，停止递归
        ans中的k-1数就是答案
    复杂度分析：
        时间：OK，遍历到第K个节点
        空间：OK，递归栈
    """
    ans = []
    def inorder(root):
        if root == None:
            return None
        inorder(root.left)
        ans.append(root.val)
        if len(ans) == k:
            return
        inorder(root.right)
    inorder(root)
    return ans[k - 1]

def kthSmallest1(self, root, k):
    """
    My Method 2
    用非递归的方式中序遍历BST，
    则递归的第k次的数就是目标值
    """
    stack = []
    counter = 0
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        counter += 1
        if counter == k:
            return root.val
        root = root.right
    return None