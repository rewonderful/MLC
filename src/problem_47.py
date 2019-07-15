#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    """
    排列数的生成思路和46相似，不同的是对重复数的处理
    先把数字排序，然后在递归的时候，如果当前要处理的数字，上一次已经处理过了，那就没有继续处理的必要了，也就是
    remain[i] == remain[i-1]，因为for是从前往后的，所以逻辑是，当前状态判断当前和上一个时刻。所以也就要求i>0
    """
    def permuteUnique(self, nums):
        self.ans = []
        nums.sort()
        def dfs(permutation,remain):
            if remain == []:
                self.ans.append(permutation)
                return
            for i in range(len(remain)):
                if i > 0 and remain[i] == remain[i-1]:
                    continue
                dfs(permutation+[remain[i]],remain[:i]+remain[i+1:])
            return
        dfs([],nums)
        return self.ans
def permuteUnique(self, nums):
    """
    思路同46题，这里用一个集合set将list转化为tuple后去重，
    """

    def generate(remain, path, result, res_set):
        if remain == []:
            return
        for i in range(len(remain)):
            path.append(remain[i])
            if len(path) == len(nums) and tuple(path) not in res_set:
                result.append(path[:])
                res_set.add(tuple(path))
            generate(remain[:i] + remain[i + 1:], path[:], result, res_set)
            path.pop()
    result = []
    generate(nums, [], result, set())
    return result