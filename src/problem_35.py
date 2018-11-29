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
    # 如果没有找到，那么应该返回最大位置,因为已经跳出了while，说明low>high，应该返回low,且若target < nums[lo]，
    # 则应该target的位置就是lo，如果target>nums[lo]，那也应该返回当前的lo，lo超过数组边界了，lo == len(nums)
    return low

def searchInsert2( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            lo = mid + 1
        if target < nums[mid]:
            hi = mid - 1
    return lo
if __name__ == '__main__':
    nums=[1,3,5,6]
    target = 0
    print(searchInsert2(nums,target))