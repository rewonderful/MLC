#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def countNodes(self, root):
    """
    Disscussion Method
    算法：递归
    思路：
        非常巧妙！
            利用完全二叉树和满二叉树的性质，首先满二叉树是完全二叉树的一种特殊情况，即所有位置的节点都不为
        空，一颗深度为K的满二叉树其节点总数为2^(k)-1,这个很好算，联想二进制求和1+2+4+8 =15，也就是16-1
        0001+0010+0100 = 0111 = 1000-1
            所以利用满二叉树的性质可以很快地用公式将节点数计算出来
            这里要做的就是如何从一颗完全二叉树中分离出满二叉树来
            如果一颗完全二叉树的左右子树高度相等，则左子树一定是满二叉树，
            否则的话，右子树一定是一颗满二叉树
            由此便可以将一颗完全二叉树拆成两个部分分别进行求解。并且注意到，这是将一颗完全二叉树拆解，拆解后
        的左右两部分，也一定是一颗完全二叉树（满二叉树也是完全二叉树），所以可以递归的进行拆解，即上述拆完一颗
        满二叉树下来并计算节点后可以将剩余的部分递归地继续进行分离满二叉树的过程
            所以这里要先用一个辅助函数计算树的高度，因为任意时刻拆解下来的树一定是完全二叉树所以可以利用完全
        二叉树的性质进行高度的计算，即其高度一定是左子树的高度，在getDepth中就可以只递归计算root.left,不用
        计算max(left,right)+1
            再一个是注意到完全二叉树的节点个数的计算其实是2^(k)-1次，而在将一个树拆分为处满二叉树的时候，如下图，
        从1开始拆除左侧的满二叉树时，左侧满二叉树的高度是2，按理说是2^(k)-1，但是还要加上root，也就是1那个节点，
        所以是2^k - 1+ 1= 2^k, 所以递归的时候就是2**k + countNodes(theOtherPart)
            1
           / \
          2   3
         / \  /
        4  5 6
    复杂度：
        时间：OlogN2

    """
    if root == None:
        return 0
    leftDepth = getDepth(root.left)
    rightDepth = getDepth(root.right)
    if leftDepth == rightDepth:
        return 2**leftDepth + self.countNodes(root.right)
    else:
        return 2**rightDepth + self.countNodes(root.left)
def getDepth(root):
    if root == None:
        return 0
    return getDepth(root.left)+1
