#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def combinationSum3(self, k, n):
    """
    My Method
    和77题类似，就，dfs，然后每次range向后挪1，path + [i]将i加入到path中，最后k == 0 且 target == 0时
    说明sum(path) == n，可以append到result中
    """
    self.result = []

    def dfs(num, k, target, path):
        if num == 10:
            return
        if k == 0 and target == 0:
            self.result.append(path)
            return
        for i in range(num + 1, 10):
            if i <= target:
                dfs(i, k - 1, target - i, path + [i])

    dfs(0, k, n, [])
    return self.result