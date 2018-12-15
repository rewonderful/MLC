#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from  TreeNode import TreeNode


class Codec:
    """
    My Method(Inspired By XiaoXiang)
        ⚠️序列化好说，就是怎么遍历和记录的问题，关键是反序列化以及如何安排二者使得序列化与反序列化搭配工作！
        序列化的过程中，用先序遍历记录头结点来
        反序列化的过程中，再利用BST的有序特性划分左右子树，就相当于给了先序遍历的结果和中序遍历的结果
    ❗️❗️❗️：
            这里和平衡二叉树不一样！所以不能用中序遍历记录二叉树的节点，然后再用逆中序遍历的方式重建二叉树！
        因为给的树不一定是平衡的！如BST [3,4,5,6,7],那么根节点应该是3，然后都是只有右孩子，而不是以中间节
        点5为根节点，虽然5为根节点可以构成平衡BST，但是这里人家给的就不是平衡的，如此一来应该考虑用更一般化
        的方法！即下面我用的记录先序遍历结果，然后根据先序和中序遍历来重构！
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        前序遍历BST，None节点用字符串'None'表示，节点之间用逗号','分割
        """
        buff = []

        def preorder(root):
            if root == None:
                buff.append('None' + ',')
                return
            buff.append(str(root.val) + ',')
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ''.join(buff)[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        先将字符串转化为列表，并且将字符串的值转为int or None
        重建的过程中类似于有了先序遍历的结果和中序遍历的结果来重建二叉树
        先序遍历的结果就是根的顺序，就是data_list
        然后利用BST的特性，当前节点node后面的第一个大于node的下标right_index就是右子树的分隔位置
        [3,1,None,2,4],
        则 root -->3,
           left--> [1,None,2]
           right-->[4]
        后面就和用preorder 和inorder 构建二叉树一样了
        """
        data_list = data.split(',')
        data_list = [int(item) if item != 'None' else None for item in data_list]

        def reConstruct(data):
            if data == []:
                return None
            root_val = data.pop(0)
            if root_val == None:
                return None
            root = TreeNode(root_val)
            right_index = len(data)
            for i in range(len(data)):
                if data[i] > root_val:
                    right_index = i
                    break
            root.left = reConstruct(data[:right_index])
            root.right = reConstruct(data[right_index:])
            return root

        return reConstruct(data_list)
if __name__ == '__main__':
    n1 = TreeNode('3')
    n2 = TreeNode('1')
    n4 = TreeNode('4')
    n5 = TreeNode('2')
    n1.left = n2
    n1.right = n4
    n2.right=n5
    # data =serialize(n1)
    # data_list = data.split(',')
    # data_list = [int(item) if item != 'None' else None for item in data_list]
    # print(data_list)