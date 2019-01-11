#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from TreeNode import TreeNode
from  BinaryTree import BinaryTree


def isValidBST(self, root):
    """
    My Method 2
    Solution Method 也是这个思路
    算法：递归
    思路：
        在递归的过程中判断左右是否满足要求
        递归的时候用min_border和 max_border记录当前位置最小不能小于多少，最大不能大于多少
        左侧节点应该小于当前根节点，但是不能小于min_border，比如下面的这个3，3小于4，但是3不应该小于5
        同理，右侧节点的值应该大于当前根节点，但是不能大于最大的max_border
                5
               / \
              1   4
                 / \
                3   6
        往左子树传的时候，更新最大上界为root.val，最小上界不变，往右子树传的时候更新最小上界为root.val,最大上界不变
            所以向下传的时候，向左侧传的话，就会更新max_border为root.val 左子树中的值再小也不能小于min_border
        同理，向右子树传的时候，更新min_border 为root.val，右子树中的值再大也不能大于max_border,二者是交替的，
        然后更新min的时候max保持不变
        3是4的左子树，3小于4，但是再小也不能小于5，min_border是上一层的root.val = 5

        在最一开始的时候，上下界是没关系的，可以认为是正负无穷，所以传inf
    复杂度：
        时间：OK，第K个节点是不满足条件的话，停止
        空间：OK，递归栈空间
    """

    def check_valid(root, min_border, max_border):
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        left_check = right_check = True
        if root.left != None:
            if root.left.val >= root.val or root.left.val <= min_border:
                return False
            else:
                left_check = check_valid(root.left, min_border, root.val)
        if root.right != None:
            if root.right.val <= root.val or root.right.val >= max_border:
                return False
            else:
                right_check = check_valid(root.right, root.val, max_border)
        return left_check and right_check

    return check_valid(root, float('-inf'), float('inf'))


def isValidBST_bfs(self, root):
    """
    Solution Method 2
    将 DFS转为BFS，用队列按层遍历，剩下的思路和上面是一样的
        用栈也行，只不过用栈的话先压右子树再压左子树，这样访问的时候就是左右了
    访问当前节点为root构成的子树时。要确认root，root.left.val，root.right.val的值的状态，每个root
    处都有一个lower_limit和upper_limit，所以用队列/栈按层访问也是一样的，毕竟相当于是判断一个局部状态
    """
    if not root:
        return True

    queue = [(root, None, None), ]
    while queue:
        root, lower_limit, upper_limit = queue.pop(0)
        if root.left:
            if root.left.val < root.val:
                if lower_limit and root.left.val <= lower_limit:
                    return False
                queue.append((root.left, lower_limit, root.val))
            else:
                return False
        if root.right:
            if root.right.val > root.val:
                if upper_limit and root.right.val >= upper_limit:
                    return False
                queue.append((root.right, root.val, upper_limit))
            else:
                return False
    return True
def isValidBST1(self, root):
    """
    My Naive Method
    算法：遍历
    思路：
        很朴素的思路，利用二叉搜索树的特性，中序遍历得到的序列一定是有序序列，所以我就中序遍历一次，得到
        值的列表result
        然后再遍历result检查，如果result不是有序数组的话，就说明Tree一定不是一颗二叉搜索树
        其实效率还可以，遍历一次所有的节点ON，然后检查数组也是ON，总体的时间是ON
    复杂度分析：
        时间：ON
        空间：ON
    """
    result = []

    def inorder(root):
        if root == None:
            return
        inorder(root.left)
        result.append(root.val)
        inorder(root.right)

    inorder(root)
    if len(result) in (0, 1):
        return True
    for i in range(1, len(result)):
        if result[i] <= result[i - 1]:
            return False
    return True
if __name__ == '__main__':
    tree = BinaryTree()
    root = tree.get_test_tree()
    isValidBST(root)