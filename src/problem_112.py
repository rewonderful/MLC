#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from TreeNode import  TreeNode


class Solution:
    def __init__(self):
        self.find = False #建立全局变量find，不然后面就得用列表find来记录True,False
    def hasPathSum(self, root, sum):
        """
        算法：先序遍历
        思路：
                遍历二叉树，把路径之和记录下来，当前节点是叶子节点的时候，将前面的路径之和+叶子节点
            的值和sum比较，相等的话置self.find = True,为了回溯回来的时候不改变当前路径的path_sum
            值，在左右遍历的时候，才向下传加上本节点val后的值
                要注意的是我这里在init中设置了一个全局变量find来保障能将递归中的结果返回出函数
            因为bool属于不可变数据类型， 不像列表，在函数中改变后会直接将结果带出去，如果我这里用普通的
            find = True，函数会在find= True那里新建一个局部变量，并且令这个局部变量的值等于True，没办法
            带出去，虽然说用global按理说会带出去，但是我试了一下还是没带出去，挺懵逼的，可能是因为函数
            递归的过没有带出去吧
                后面的完全递归版本更好地理解递归中如何将结果返回，怎样return
        复杂度分析：
            时间：ON，每个节点只访问一次
            空间：ON，所有节点都要遍历，递归栈空间
        """
        def pre_travel(root, path_sum):
            if root == None:
                return
            else:
                if root.left == None and root.right == None:
                    if path_sum + root.val == sum:
                        self.find = True

                pre_travel(root.left, path_sum + root.val)
                pre_travel(root.right, path_sum + root.val)

        pre_travel(root, 0)

        return self.find

    def hasPathSum2(self, root, sum):
        """
        完全递归版本v1
        一开始没改对的原因是因为，return没把握好，如果只有if root == None 那里的一个return
        事实上这儿的return只是终止在叶子节点的递归罢了，而上层，返回递归调用的地方
        self.hasPathSum(root.left,sum-root.val ) -->下一层return了一个self.find
        self.hasPathSum(root.right,sum-root.val) -->下一层return了一个self.find
        然后函数执行结束，也就是左右遍历后并没有将左右遍历的结果返回回去，所以输出是None
        所以最后应该return一下，这里return 二者的or也可以或者return self.find也可以，反正
        最后返回的就是self.find而且其只可能被该为True
        """
        if root == None:
            return self.find
        else:
            if root.left == None and root.right == None:
                if sum - root.val == 0:
                    self.find = True
        return self.hasPathSum(root.left,sum-root.val ) or self.hasPathSum(root.right,sum-root.val)
    def hasPathSum3(self, root, sum):
        """
        完全递归版本v2
        ....
        所以最后应该return一下，这里return 二者的or也可以或者return self.find也可以，反正
        最后返回的就是self.find而且其只可能被该为True
        """
        if root == None:
            return self.find
        else:
            if root.left == None and root.right == None:
                if sum - root.val == 0:
                    self.find = True
            self.hasPathSum(root.left, sum - root.val)
            self.hasPathSum(root.right, sum - root.val)
        return self.find
if __name__ == '__main__':
    #[5,4,8,11,null,13,4,7,2,null,null,null,1]

    n1 = TreeNode(5)
    n2 = TreeNode(4)
    n3 = TreeNode(8)
    n4 = TreeNode(11)
    n5 = TreeNode(13)
    n6 = TreeNode(4)
    n7 = TreeNode(7)
    n8 = TreeNode(2)
    n9 = TreeNode(1)

    n1.left = n2
    n1.right = n3
    n2.left=n4
    n4.left=n7
    n4.right=n8
    n3.left=n5
    n3.right=n6
    n6.left=n9
    s = Solution()

    print(s.hasPathSum(n1,22))
