#!/usr/bin/env python
# _*_ coding:utf-8 _*_
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