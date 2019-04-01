#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
https://www.jianshu.com/p/2e5edb21d0ff
题目：
    给一个数组，返回一个大小相同的数组。返回的数组的第i个位置的值应当是，
对于原数组中的第i个元素，至少往右走多少步，才能遇到一个比自己大的元素（如果之后没有比
自己大的元素，或者已经是最后一个元素，则在返回数组的对应位置放上-1）。
"""
def monotonousStack(nums):
    ans = [-1]*len(nums)
    stack = []
    for i in range(len(nums)):
        while stack !=[] and nums[i] > nums[stack[-1]]:
            index =stack.pop()
            ans[index] = i - index
        stack.append(i)
    return ans
if __name__ == '__main__':
    testcase = [5,3,1,2,4]
    testcase2 = [9, 3, 5, 8, 2, 6]

    print(monotonousStack(testcase2))
    #ans : [-1 3 1 1 -1]
    #      [-1,1,1,-1,1,-1]