#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    """
    remain == []的时候说明一条排列已经生成了，append就好
    递归，其实就是一种特殊的循环，这种循环遍历的是一种树形结构，不是for循环那样的线性结构，

    """
    def permute(self, nums):
        self.ans = []
        def dfs(permutation,remain):
            if remain == []:
                self.ans.append(permutation)
                return
            for i in range(len(remain)):
                dfs(permutation+[remain[i]],remain[:i]+remain[i+1:])
        dfs([],nums)
        return self.ans
def permute0( nums):
    """
    My Method
    算法：递归/回溯
    思路：
        就像人写排列一样，对[1,2,3]，固定1后，第二次选2，第三次选3，或者第二次选3，第三次选2
        这里采用一样的方法，for循环对当前remain中剩余的元素，每次放一个进path，然后将剩下的元素
        传到下一层，递归进行，要注意的是generate后要pop来保证当前层path的不同，如当前层是[]，追加
        了1后，当1打头的都生成完后回到这里应该pop，使得path是空[]，从而继续添加[2]开头的
    复杂度分析：
        时间：不会算
        空间：不会算
    """

    def generate(remain, path, result):
        if remain == []:
            return
        for i in range(len(remain)):
            path.append(remain[i])
            if len(path) == len(nums):
                result.append(path[:])
            generate(remain[:i] + remain[i + 1:], path[:], result)
            path.pop()

    result = []
    generate(nums, [], result)
    return result
def permute1( nums):
    """
    同permute0，只不过这里传参数的时候传入[remain[i]] + path，并且添加result的操作在开始的时候
    """

    def generate(remain, path, result):
        if len(path) == len(nums):
            result.append(path[:])
        if remain == []:
            return
        for i in range(len(remain)):
            generate(remain[:i] + remain[i + 1:], [remain[i]] + path, result)

    result = []
    generate(nums, [], result)
    return result
if __name__ == '__main__':
    print(permute0([1,2,3]))