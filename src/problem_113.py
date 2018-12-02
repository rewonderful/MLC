#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def pathSum( root, sum):
    """
    算法：递归先序遍历
    思路：
        类似112，只不过这里要记录和为sum的路径罢了
        同样在传参的时候用path + [root.val]往下传来保障这一层在回溯的时候path没有被改变
        这样加号+传的会新建一个变量往下传从而不会影响当前层的path值
    复杂度分析：
        时间：ON，遍历所有节点
        空间：ON，遍历所有节点需要的递归栈的空间以及result的空间
    """

    def pre_travel(root, path_sum, path):
        if root == None:
            return
        else:
            if root.left == None and root.right == None:
                if path_sum + root.val == sum:
                    result.append(path + [root.val])

            pre_travel(root.left, path_sum + root.val, path + [root.val])
            pre_travel(root.right, path_sum + root.val, path + [root.val])

    result = []
    pre_travel(root, 0, [])
    return result