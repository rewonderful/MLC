#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def binarySearch(nums,target):
    l,r = 0,len(nums)-1
    if len(nums) == 0 :
        return -1
    while l <= r :
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# def binarySearch(nums,target):
#     lo = 0
#     hi = len(nums) - 1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if nums[mid] == target:
#             return mid
#         elif target > nums[mid]:
#             lo = mid + 1
#         else:
#             hi = mid - 1
#     return - 1


if __name__ == '__main__':
    nums = [1,2,3,4,5,9,11,13,222,333,444,555]
    target = 5
    print(binarySearch(nums,target))