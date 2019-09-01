#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def combine2(self, n: int, k: int):
    """
    :param self:
    :param n:
    :param k:
    :return:
    一定是顺序往后的，就相当于每个节点为根节点，然后进行dfs的遍历。所以要理解树是特殊的图，dfs
    本来是图中的概念，现在也可以直接用进来。就是每一刻的子空间都是在某个位置取选取一个元素，添加到
    路径中。当len(path) == k的时候，就说明递归深度达到了我们的目标
    """
    self.ans = []
    def dfs(i, path):
        if len(path) == k:
            self.ans.append(path[:])
            return
        for j in range(i + 1, n + 1):
            dfs(j, path + [j])
        return

    for i in range(1, n - k + 2):
        dfs(i, [i])
    return self.ans
"""
或者👇，是把上面的for循环提出来了。上面的for循环其实相当于是剪枝，因为有的部分已经不能做根节点了，下面这种会更简洁
"""
def combine3(self, n: int, k: int) :
    self.ans = []

    def dfs(i, path):
        if len(path) == k:
            self.ans.append(path[:])
            return
        for j in range(i + 1, n + 1):
            dfs(j, path + [j])
        return

    dfs(0, [])
    return self.ans
def combine(self, n, k):
    """
    My + Disscussion Method
    从某个位置开始回溯搜索，用k 记录每次允许的长度，当k ==0 时达到要求长度，添加到result中，因为每次都是for循环
    中依次start + 1后移的，所以不会重复，也就不用额外地做去重工作。
    然后要注意的是外面dfs(0, k, [])是从0开始的，这样递归的过程中里面就会从1开始，或者也可以在外面
    for num in range(1,n+1):
        dfs(num,k-1,[num])
    这样来调用
    """
    self.result = []

    def dfs(start, k, path):
        if k == 0:
            self.result.append(path[:])
            return
        for num in range(start + 1, n + 1):
            dfs(num, k - 1, path + [num])

    dfs(0, k, [])
    return self.result
