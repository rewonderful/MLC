#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def rotate(self, nums, k):
    """
    先将整个数组旋转
    然后再将前k个部分旋转
    再将k到n-1旋转
    [1, 2, 3, 4, 5, 6, 7]，k=3
            👇
    [7, 6, 5, 4, 3, 2, 1]
            👇
    [5, 6, 7, 4, 3, 2, 1]
            👇
    [5, 6, 7, 1, 2, 3, 4]

    测试样例的k可能超过len(nums)，所以取余
    """
    def reverse(i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    k = k % len(nums)
    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)