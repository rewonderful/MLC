#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from TreeNode import TreeNode
def postorderTraversal(self, root):
    """
    记住得了= =
    就访问当前root，然后左子树入栈，右子树入栈，最后逆序一下就好了，return output[::-1]
    相当于是这么个思路：
        目标：左右根
        那么我就先求出来根右左，先根遍历是好访问的，根右左的话，因为是栈，所以先访问根，然后左孩子节点入栈，
        再右孩子节点入栈，这样出栈的顺序就是跟右左了，其实可以联想一下，其实左右只是人为设定和规定的嘛，就像二分类要用10，也可以看成是01
        一个道理，那就调换左右顺序呗，这样就可以根右左的访问
        最后再将【根右左】遍历得到的结果逆序，不就是左右根了，比较讨巧
    """
    if root is None:
        return []

    stack, output = [root, ], []
    while stack:
        root = stack.pop()
        output.append(root.val)
        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)

    return output[::-1]

def postorderTraversal2(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    ans = []
    visited = set()
    stack = [root]
    while stack:
        top = stack[-1]
        if top in visited:
            ans.append(stack.pop().val)
        else:
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
            visited.add(top)
    return ans

def postorderTraversal1(self, root):
    """
    算法：递归遍历
    """
    return [] if root == None else self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
if __name__ == '__main__':
    #1,2,3,4,5,6,7
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    # t1.left = t2
    # t1.right = t3
    # t2.left = t4
    # t2.right = t5
    # t3.left  = t6
    # t3.right = t7
    t1.right =t2
    t2.left = t3

    print(postorderTraversal(t1))

