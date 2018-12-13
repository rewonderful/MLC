#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from TreeNode import TreeNode


def deleteNode(self, root, key):
    """
    XiaoXiang Method
    算法：？
    思路：
        先找到节点，然后再对要删除的节点进行处理
        找到节点好说，用BST的性质找就好了
        主要在于如何处理
        这里的方法比较笨也比较麻烦，
            1. 先确定当前root是prev的左孩子还是右孩子，后面重构prev要用
            2. 如果左子树为空，将右子树顶上来，如果右子树为空，左子树顶上来
            3. 左右子树都不为空时，将右子树的最左节点替换为当前root节点，这样处理后，仍是BST
            ❗️右子树的最左节点，一定大于原root的所有左子树节点，也一定小于原root的所有右子树节点，所以用右子树最左节点替换
                而右子树又分几种情况：
                    1.右子树是叶子节点，直接替换
                    2.右子树有左子树
                        找到最左节点p和最左节点的上一个节点p_prev
                        如果p_prev != root
                        root->  5
                                \
                                8 <- p_prev
                              /  \
                         p-> 6    9
                              \
                               7
                            令root.val = p.val，并且p_prev.left = p.right
                        否则
                                8 -> root(p_prev)
                              /  \
                          p->6    9
                            令root.right = p.right
        调整完右子树后，将右子树与prev再连接起来
        注意如果删除的是整棵树的根节点，最后要直接return adjust的结果，调整后的节点就是根节点，
        否则返回原root，此时原root已被修改
    注意❗️：
        不能在递归中进行adjust操作，否则的话，如果操作的是根节点，根节点的变动不会被引用赋值传到外面！
        因为递归栈的原因！
        当前层root = None，然后传导到上一层调用之的地方，root = 3，下一层修改的root = None被抹除了!
        所以我这里分开来处理来避免无法将值带出的问题，其实主要是当要修改的就是顶层根节点的时候会出这个问题！
        先findeNode找到node和prev，在adjuest对node和prev做修改
        最后返回整个root

    复杂度分析：
        时间：找节点logN，调整节点OK
        空间：logN，递归栈
    """

    def adjust(root, prev):
        left = prev != None and prev.left == root
        right = prev != None and prev.right == root
        if root.left == None:
            root = root.right
        elif root.right == None:
            root = root.left
        else:
            p = root.right
            if p.left == None and p.right == None:
                root.val = p.val
                root.right = None
            else:
                p_prev = root
                while p.left:
                    p_prev = p
                    p = p.left
                if p_prev != root:
                    p_prev.left = p.right
                else:
                    p_prev.right = p.right
                root.val = p.val
            del p
        if left:
            prev.left = root
        elif right:
            prev.right = root
        return root

    def findNode(root, prev):
        if root == None:
            return None, prev
        if root.val == key:
            return root, prev
        if key < root.val:
            return findNode(root.left, root)
        else:
            return findNode(root.right, root)

    node, prev = findNode(root, None)
    if node != None:
        curr = adjust(node, prev)
        if prev == None:
            return curr
    return root

def deleteNode1(self, root, key):
    """
    Disscussion Method
    思路：
        和上述 XiaoXiang Method 一样！
        但是代码写得更漂亮！
        好好品一下
    """
    if not root:
        return None
    if key > root.val:
        # 注意体会一下运用递归重新构建二叉树的过程，
        # 通过这种方式，可以将二叉树从下往上重新构建一遍，最后返回根元素
        root.right = self.deleteNode(root.right, key)
        return root
    elif key < root.val:
        root.left = self.deleteNode(root.left, key)
        return root
    else:
        # 待删除如果左子树为空
        if not root.left:
            rightNode = root.right
            root.right = None
            # 把右侧节点返回去，重新挂回树上
            return rightNode
        # 待删除如果右子树为空
        if not root.right:
            leftNode = root.left
            root.left = None
            return leftNode
        # 如果左右子树都存在的情况下
        # 找到待删除节点右子树中的最小元素，然后替换待删除元素
        successor = self.minimum(root.right)
        # 删除右子树中的最小值，并返回右子树的根节点
        successor.right = self.removeMin(root.right)
        successor.left = root.left
        return successor

def minimum(self, root):
    if not root.left:
        return root
    return self.minimum(root.left)

def removeMin(self, root):
    if not root.left:
        rightNode = root.right
        root.right = None
        return rightNode
    root.left = self.removeMin(root.left)
    return root
if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.right = n2
    print(deleteNode(n1,1))