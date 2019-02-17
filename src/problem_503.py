#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def nextGreaterElements(self, nums: 'List[int]') -> 'List[int]':
    """

    """
    ans = [-1] * len(nums)
    stack = []

    for i in range(len(nums) * 2):
        while stack and nums[stack[-1]] < nums[i % len(nums)]:
            ans[stack.pop()] = nums[i % len(nums)]
        stack.append(i % len(nums))
    return ans