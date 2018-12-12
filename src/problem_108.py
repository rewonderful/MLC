#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from TreeNode import TreeNode
def sortedArrayToBST( nums):
    """
    算法：递归
    思路：
        关键在于如何构造这颗二叉查找树（BST）可以让左右的高度相差不高于1，就是平衡二叉树的概念
        如果每次以数组的中间节点来构造这颗BST，那么其左右数组的元素就是相等或者相差1的，就可以实现
        高度相差1 ！！
            如奇数个元素，1,2,3,4,5，以3为根，左子树[1,2]两个元素，右子树[4,5]两个元素，肯定是平衡的
            如偶数个元素，1,2,3,4,5,6，以3为根，左子树[1,2]两个元素，右子树[4,5,6]三个元素，相差为1，平衡的
        而一个数组不是奇数个元素就是偶数个元素，并且以重点划分后其左右子数组(子树)的长度也一定是奇数或偶数的，并且
        也一定是排序好的数组，只不过规模更小了罢了，所以也一定能将其分解为平衡的子树，并且从最上面的根节点的角度来看，
        其左右子树的元素数量差一定不大于1(其实从每个子数组，子树来看，也是一样)，所以这样构造BST即可构造一颗平衡二叉树！
    复杂度分析：
        时间：ON，遍历所有节点
        空间：ON，递归栈空间，以及建立节点的空间
    """
    if nums == []:
        return None
    center = len(nums) // 2
    root = TreeNode(nums[center])
    root.left = sortedArrayToBST(nums[:center])
    root.right = sortedArrayToBST(nums[center:])
    return root

def sortedArrayToBST1(self, nums):
    """
     以下算法为用二叉树搜索，其效率更高！
     因为不用切片取左右子区间了
     并且
     该算法更加通用，在没有切片操作的语言中也可以用
     下面的
        if lo == hi XXX
        是"剪枝"操作，lo==hi时就是叶子节点了，无需向下递归，直接return就好
    """

    def constructBST(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        root = TreeNode(nums[mid])
        if lo == hi:
            return root
        root.left = constructBST(lo, mid - 1)
        root.right = constructBST(mid + 1, hi)
        return root

    return constructBST(0, len(nums) - 1)
if __name__ == '__main__':
    print(sortedArrayToBST([-10,-3,0,5,9]))



