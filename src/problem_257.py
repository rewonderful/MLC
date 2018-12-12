#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def binaryTreePaths(self, root):
    """
    My Method
    """
    result = []

    def dfs(root, path):
        if not root:
            return
        path = path + '->' + str(root.val) if path != '' else str(root.val)
        if root.left == None and root.right == None:
            result.append(path)
        dfs(root.left, path)
        dfs(root.right, path)
    dfs(root, '')
    return result

def binaryTreePaths1(self, root):
    """
    Disscusion Method
    这种列表生成式的做法更巧妙！
    人家构造的return的值好！
    而且这样显式构造列表[]，不会存在浅拷贝的问题，因为每次递归都声明了一个新的列表对象
    """
    if not root:
        return []
    if not root.left and not root.right:
        return [str(root.val)]
    treepaths = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)]
    treepaths += [str(root.val) + '->' + path for path in self.binaryTreePaths(root.right)]
    return treepaths