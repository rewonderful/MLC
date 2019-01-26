#!/usr/bin/env python
# _*_ coding:utf-8 _*_
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
