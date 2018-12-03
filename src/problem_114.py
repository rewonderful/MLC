#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from TreeNode import TreeNode
def flatten0( root):
    """
    My Method
    算法：递归
    思路：
            回想链表逆置的递归做法，某个位置的root.next=递归函数的返回值连接起来（题目中要原地操
        作，而且返回是void，所以在函数内建一个有返回值的递归函数去完成拼接)
            这里也是相似的想法，其实对一个二叉树转链表，就是递归地把左子树变成链表，把右子树变成
        链表，然后把左右子树拼接起来(所以有while)，而每个左子树和每个右子树都有其左右子树，所以
        有(if root.left != None else，这样两侧对root.left和root.right的操作)
        如果左子树不为空，左右子树都要处理，如果左子树为空，就单拉直右子树
        递归到最底下的时候，其实一颗底部的二叉树无外乎以下三种样子
             root              root           root
            /   \             /                  \
         left   right      left                  right

        从底部来看就清楚很多了，当前在root，那么把左边调整到右边的方法就是
            1.如果左右都不为空，调整右子树拉直，调整左子树拉直，将拉之后的左子树插到右子树前
              由于左子树拉直后可能含多个节点，所以插右子树的时候要用while找到左子树的尾部
            2.左子树不为空，右子树为空，其实也要调整右子树，但是调整方式很简单，递归到右子树
              的时候，判断是None，返回None就好了，然后同1，插入左子树
            ps: 其实1，2都可以看做是一种情况，就是左边为不为空，本题关注的就是这个
            3.如果左边为空，那左边不用插到右边，调整右边就好了，把右边调整好return的节点插到root.right上

                所以根据以上1,2,3分析也可以很容易想到adjust刚开始的判断，如果root为空就返回None，如果root是
            叶子节点，返回它自己即可
        注意：
            递归函数弄清楚返回值的情况很重要！！比如这里我的解法后面if else之后一定要return root
        这里的root已经是拉成单链表后的root了，如果不return的话，前面调用的adjust时就会返回None！
        一定要注意递归写法中的return！
    复杂度分析：
        时间：ON，遍历所有节点
        空间：ON，递归栈空间
    """

    def adjust(root):
        if root == None or (root.left == None and root.right == None):
            return root
        if root.left != None:
            tmp = adjust(root.right)
            root.right = adjust(root.left)
            p = root.right
            while (p.right != None):
                p = p.right
            p.right = tmp
            root.left = None
        else:
            root.right = adjust(root.right)
        return root

    adjust(root)

def flatten1( root):
    """
    算法：递归
    思路：
            主要思路和My Method一样，，只不过我的做法My Method中要借助一个有返回值的辅助函数来将拉
        直后的左右子树插到当前的root节点左右，事实上不需要一个有返回值的辅助函数就可以完成左右端节点
        的调换(我还是觉得My Method思路更直观一些)
                root              root           root
               /   \             /                  \
            left   right      left                  right
            本方法的思路就是直接原地将左子树接到右子树上，由于Python传参的特性，TreeNode传参时传的是
        引用，相当于指针，即函数中对root的改变会带出去，所以在子树中进行的调整，已经将这个结果带到了外
        面的函数中
            递归到在底部调整后，原树在底部的结构已经改变，再回溯回去返回到最上层的root，left,right
        此时的left和right已经拉直了，令p.right=tmp完成最顶部的左右子树链接即可
    复杂度分析：
        时间：ON，遍历所有节点
        空间：ON，递归栈空间
    """
    if not root: return
    flatten1(root.left)
    flatten1(root.right)
    temp = root.right
    root.right = root.left
    root.left = None
    p = root
    while p.right != None:
        p = p.right
    p.right = temp

def flatten2(root):
    """
    My Method
    算法：暴力/其实不满足题目的要求，因为不是原地改变了
    思路：
        前序遍历二叉树将节点记录下来，然后依次用right连接起来
    复杂度分析：
        时间：ON，dfs遍历N个节点，后面遍历列表也要ON
        空间：ON，递归栈空间，辅助存储的列表空间
    """
    if root == None:
        return
    nodes = []

    def dfs(root):
        if root == None:
            return
        nodes.append(root)
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    for i in range(len(nodes) - 1):
        nodes[i].right = nodes[i + 1]
        nodes[i].left = None
def preoredr(root):
    if root == None:
        print(None)
        return
    print(root.val)
    preoredr(root.left)
    preoredr(root.right)
if __name__ == '__main__':
    """
        1
       / \
      2   5
     / \   \
    3   4   6
    """
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n1.left = n2
    n1.right = n5
    n2.left = n3
    n2.right = n4
    n5.right = n6
