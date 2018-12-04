#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from TreeNode import TreeNode
def buildTree(self, preorder, inorder):
    """
    算法：递归
    思路：
        其实和本科上课时学到的人工根据先序遍历和中序遍历构造二叉树的思路是一样的。
        （一定不能没有中序遍历的序列否则无法判断左右子树）
            在先序序列中找到根节点，然后去中序遍历序列中找到根节点的位置将中序遍历序列以root
        为界分成左右两个子树，然后递归，从左子树开始继续从先序遍历的列表中依次取出根节点，
        将传进来的左子树的中序遍历列表按先序的跟划分为其左右子树，若其左右子树为空，则返回None，
        何为左右子树为空？即以它为分割，在中序遍历里面该节点的左右都为0呗，或者一方为0，就是None嘛。
        同理右子树也根据此思路递归去构建即可，最后返回root
        注意：
            1.这里要注意的是，如何确定向下一层递归的时候，传给下一层的preorder和inorder是怎样的，
        对inorder来说很好讲，传左右侧的切片，对preorder来说，其实要传的就是它本身，或者说是一个全局
        的preorder，因为在左子树遍历的过程中，就应该把preorder中左子树的节点都弹出了，这样才能保障
        在构建root的右子树时，preorder的首部preorder[0]或者说队列preorder的首部就是右子树的根节点，
        根据python的传参特点，直接向下传preorder就好了，不要传切片
            2. 向下递归的时候，一定要从左子树开始构建！可以对比106题来更好地理解这一点，因为先序遍历
        时是"根-->左-->右"，即根元素的右边近邻着的是左子树，所以pop根的顺序其实隐含了是从左侧开始pop，
        每次弹出的其实都是左侧的节点，所以重建的时候，因为preorder是一个"全局变量"，所以先构建完左子树，
        再把构建完后已经产生变化，将左子树节点都pop掉的preorder传给右子树进行右子树的构建，此时就可以
        保证右子树中访问的preorder的元素都是右子树的元素了
    复杂度分析：
        时间：ON2，inorder.index寻找下标的操作要ON，嵌套递归ON，总ON2
        空间：ON，存储整个树节点，且递归栈也有空间
    """
    if inorder == []:
        return None
    root_val = preorder.pop(0)
    root = TreeNode(root_val)
    index = inorder.index(root_val)
    root.left = self.buildTree(preorder, inorder[:index])
    root.right = self.buildTree(preorder, inorder[index + 1:])
    return root