#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def isSubtree(self, s, t):
    """
    遍历去检查，首先定义equals
    如果两个树每个节点的取值都相同，那么这两棵树就是相等的，
    然后定义dfs去遍历，当遍历到某个位置s.val == t.val的时候,就可以在此时，以子树s和t进行equals判断
    如果equals为True的话，返回True
    否则的话，继续dfs s的left和s.right
    """

    def equals(x, y):
        if x == None and y == None:
            return True
        if x == None or y == None:
            return False
        if x.val != y.val:
            return False
        return equals(x.left, y.left) and equals(x.right, y.right)

    def dfs(s, t):
        if s == None:
            return False
        if s.val == t.val and equals(s, t):
            return True
        return dfs(s.left, t) or dfs(s.right, t)

    return dfs(s, t)
def isSubtree1(self, s, t):
    """
    将两棵树转为字符串，然后判断t构成的字符串是不是s构成字符串的子串
    要注意在val前面加上#来分割单个数字，避免两个节点如#2#4被当做是#24

    左孩子None和右孩子None也要做区分，不然可能会将错误的树结构当成是子树
    """

    def preorder(root, isleft):
        if root == None:
            return 'lnone' if isleft else 'rnone'
        return '#' + str(root.val) + ' ' + preorder(root.left, True) + ' ' + preorder(root.right, False)

    t1 = preorder(s, True)
    t2 = preorder(t, True)
    return t2 in t1