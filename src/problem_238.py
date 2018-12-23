#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def productExceptSelf(self, nums):
    """
    My Method (part from disscussion)
    算法：左右两次遍历
    思路：
        ！！首先要注意不能用除法，所以乖乖地按题意来
        理解题意：
            除了自己的乘积，就是当前curr的左侧的乘积去乘右侧的乘积，所以先从左到右乘一遍，再从右到左乘一遍
            先从左到右遍历一遍，result记录每个位置i处的从[0:i]的左侧位置的所有元素的乘积
            再从右到左遍历一遍，更新result[i]为左侧的乘积乘右侧的乘积，这个时候因为result[i]内已经有数字了，
            所以要单独用一个right_product记录右侧数字的乘积，然后到了每个i位置后更新right_product
    复杂度分析：
        时间：ON，两次单层for
        空间：O1，常数级
    """
    result = [0] * len(nums)

    result[0] = 1
    for i in range(1, len(nums)):
        result[i] = result[i - 1] * nums[i - 1]
    right_product = 1
    for j in range(len(nums) - 1, -1, -1):
        result[j] = result[j] * right_product
        right_product *= nums[j]
    return result
if __name__ == '__main__':
    print(productExceptSelf([0,2,3,4]))