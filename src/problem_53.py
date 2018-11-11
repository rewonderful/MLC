#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def maxSubArray( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #相当于是用当前值去加历史值，如果历史值小于0，负值，那么就应该抛弃历史序列，
    # 因为当前值（不论正负）加负值是一定比当前值更小的
    num_sum = 0
    max_sum = -float("inf")
    for num in nums:
        num_sum += num
        if num_sum > max_sum:
            max_sum = num_sum
        if num_sum < 0:
            num_sum = 0
    return max_sum
if __name__ == '__main__':
    nums = [1,-1,2,-2]
    maxSubArray(nums)