#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def searchInsert0( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i in range(len(nums)):
        element = nums[i]
        if element == target:
            return i
        elif element > target:
            return i
    return len(nums)

def searchInsert( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums) - 1
    if len(nums) == 0:
        return 0
    if target > nums[high]:
        return len(nums)
    while (low <= high):
        mid = int((low + high) / 2)
        mid_num = nums[mid]
        if mid_num == target:
            return mid
        if target > mid_num:
            low += 1
        else:
            high -= 1
    return low   #如果没有找到，那么应该返回最大位置,因为已经跳出了while，说明low>high，应该返回lows
if __name__ == '__main__':
    nums=[1,2,3,4]
    target = 5
    searchInsert(nums,target)