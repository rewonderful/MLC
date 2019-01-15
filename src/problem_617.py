#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def mergeTrees(self, t1, t2):
    """
    遍历，
    谁None就返回另外那个非None的
    如果两个都不为None，就t1.val += t2.val叠加
    然后递归构造t1.left,t1.right
    """
    if t1 == None:
        return t2
    if t2 == None:
        return t1
    t1.val += t2.val
    t1.left = self.mergeTrees(t1.left, t2.left)
    t1.right = self.mergeTrees(t1.right, t2.right)

    return t1