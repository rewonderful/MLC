#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from TreeNode import TreeNode
from BinaryTree import BinaryTree


class Codec:
    """
    Solution Method
    参考答案给的解法是将二叉树DFS序列化，然后对其反序列化
        这里我最关键的是每想到这样去反序列化，因为python传参是引用传参，通过这种先左后右虽然传
    的都是同一个data，但是其实在左子树和右子树的建立中所看到的data是不一样的，而序列化的建立过程中
    又是先左后右的，所以对一个序列用data[0]去建立节点反序列化是可以构造出原来的树的，而且这种DFS的
    方法不会像我用层次遍历一样建立很多none的空节点，效率相对来说高
    ❗️❗️❗️：
        其实第105题根据先序和中序构造二叉树也是巧妙地利用了这种传参就是传引用的特点，对二叉树进行的
    处理，可以回顾一下
        再一个是序列化的过程中要注意参数传递的意义和值，string在左右子树中就不能+=了，不然会错，因为
    此时的string 已经是+=root.val了，底下既向下传这个加后的string，又+=，就会重复导致出错
    """

    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        def preorder(root, string):
            if root == None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = preorder(root.left, string)
                string = preorder(root.right, string)
            return string

        return preorder(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def reconstructTree(data):
            if data[0] == 'None':
                data.pop(0)
                return None
            root = TreeNode(int(data[0]))
            data.pop(0)
            root.left = reconstructTree(data)
            root.right = reconstructTree(data)
            return root

        return reconstructTree(data[:-1].split(','))


class CodecTLE:
    """
    My TLE Method
    最后一个超长的case没过
    思路：
        我想的是利用满二叉树的性质，将二叉树转成一个满二叉树，这样就可以通过下标进行左右孩子的索引然后把树建立起来
        即 根为index的左孩子2*index，右孩子2*index+1
        这其中要处理好孩子节点可能是None，导致目标下标不存在，我这里的做法就是用while去不停地append None，使得
        数组的长度是能容纳得下节点数的
        在队列中存的就不仅仅是node了，还有node在满二叉树数组中的下标

        TLE的原因应该是序列化的过程中，我的这种做法会记录大量不存在的None节点，并且在反序列化的过程中，也要去考虑这些
        None的节点，导致整个树的处理时间变长，用DFS的话，建立的序列会更短
        ps:如果可以建立两个string的话，就可以记录两种序列，先序序列和中序序列，然后就可以按照先序序列和中序序列来构造二叉树了
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ''
        nodes = ['None']
        queue = [(root, 1)]
        while queue:
            node, index = queue.pop(0)
            while index >= len(nodes):
                nodes.append('None')
            nodes[index] = str(node.val)
            # nodes.extend(['None','None'])
            if node.left:
                # nodes[2*index-1] = str(node.left.val)
                queue.append((node.left, 2 * index))
            if node.right:
                # nodes[2*index] = str(node.right.val)
                queue.append((node.right, 2 * index + 1))

        return ','.join(nodes[1:])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        data = data.split(',')
        TreeNodes = [None]
        for i in range(len(data)):
            if data[i] != 'None':
                TreeNodes.append(TreeNode(int(data[i])))
            else:
                TreeNodes.append(None)
        for i in range(1, len(TreeNodes)):
            if TreeNodes[i] != None:
                if 2 * i <= len(TreeNodes) - 1:
                    TreeNodes[i].left = TreeNodes[2 * i]
                if 2 * i + 1 <= len(TreeNodes) - 1:
                    TreeNodes[i].right = TreeNodes[2 * i + 1]
        return TreeNodes[1]


if __name__ == '__main__':
    code = Codec()
    bt = BinaryTree()
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    string = code.serialize(bt.get_test_tree2())
    print(string)
    #tree = code.deserialize(string)
    # print()


