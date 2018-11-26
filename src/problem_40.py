#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def combinationSum2(self, candidates, target):
    """
    算法：递归/回溯
    思路：
            和第39题的思路相近，代码也相近，不同的是本题目中原candidates列表中有重复元素了
        并且每个元素自身不能重复使用了，只能使用duplicate次，即每个元素能使用1次，但是一个元素可能
        其相同的元素共有n个，所以解中相同元素至多能用n次
            故和39题相比，第一联想到的就是将数组先排序再做，排序后使得相同的元素挨在了一起，那么套用
        39题的思路向下传candidates[i+1:]时，如果后面是相同的元素，则至多使用其每个位置1次，而本身
        不会再被重复使用（注意39题中向下传的是candidates[i:]，这样写本身元素可以被重复使用）。然后
        要注意做去重的工作，用一个set记录tuple格式的数组就可以完成去重。并且这里sort后以及向下
        传入candidates[i+1]去判断后续的元素保障了组成同一解的元素排列是相同的，即只会有(i,j,k)，(i,j,k)
        不会有(i,j,k),(j,k,i)。

        ps:
            也尝试过不用set，去判断当前循环层candidates[0]首部元素是否和result解中最后一个解的首部元素相同，
        但是这样是错误的！如一个正确无重复的result[[1,2,5],[1,7],[1,1,6],[2,6]]，如果按解的头部重复就不加入
        解的话，那么答案会变成[[1,2,5],[2,6]]，显然错误！
    复杂度分析：
        时间：不会算。。反正肯定大于ON2小于ON2^N
        空间：不会算。。反正肯定大于ON2小于ON2^N
    """

    def find(candidates, target, path, result, res_set):
        if target < 0:
            return
        for i in range(len(candidates)):
            curr_path = path + [candidates[i]]
            if candidates[i] == target and tuple(curr_path) not in res_set:
                result.append(curr_path[:])
                res_set.add(tuple(curr_path))
            if candidates[i] < target:
                find(candidates[i + 1:], target - candidates[i], curr_path[:], result, res_set)

    result = []
    candidates.sort()
    find(candidates, target, [], result, set())
    return result