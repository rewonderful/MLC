#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def inorderTraversal(self, root):
    """
    递归
    """
    ans = []
    if root == None:
        return ans
    ans += self.inorderTraversal(root.left)
    ans += [root.val]
    ans += self.inorderTraversal(root.right)
    return ans

def inorderTraversal_ONELINE(self, root):
    return [] if root == None else self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)

def inorderTraversal_iterV1(self, root):
    """
    非递归版本
    用stack记录遍历过的节点，中序就是左根右嘛，最左子树无非就是以下几种情况
                 x              x
               /   \          /  \
             None  None     None  x
    所以这里的第二个while条件是while root,就是当root = root.right == None的时候就可以跳过了 pop了
    第一个while里有root主要是为了把第一个root添加进来，
    pop后再转到right节点判断，这不就是左根右
    """

    stack = []
    ans = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        ans.append(root.val)
        root = root.right
    return ans

def inorderTraversal_iterV2(self, root):
    """
    非递归版本V2
    这样写少一个while，逻辑和思路和V1一模一样
    """

    stack = []
    ans = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            ans.append(root.val)
            root = root.right
    return ans

def inorderTraversal1(self, root):
    """
    这种更快，因为append的时间是O(1)更快
    """
    ans = []

    def inorder(root):
        if root == None:
            return
        inorder(root.left)
        ans.append(root.val)
        inorder(root.right)

    inorder(root)
    return ans

def inorderTraversal2(self, root):
    """
    虽然AC了但这样解是不对的
    因为我这里将top与top.left的链接断开来避免死循环，这样破坏了原来的树的结构，不稳妥
    """
    if not root:
        return []
    stack = [root]
    ans = []
    while stack:
        top = stack[-1]
        while top.left:
            tmp = top.left
            stack.append(tmp)
            top.left = None
            top = tmp

        node = stack.pop()
        ans.append(node.val)
        if node.right != None:
            stack.append(node.right)

    return ans