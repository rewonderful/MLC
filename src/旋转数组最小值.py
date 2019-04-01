#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def find_min(nums):
    """

    My Method
    旋转数组内的话，第一段的数组尾部值一定大于第二段数组尾部值，所以就左右夹逼
    """

    lo = 0
    hi = len(nums)-1
    while lo < hi :
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]



if __name__ == '__main__':
    #nums = [4, 5, 6, 7, 1, 2,3]
    nums = [4, 5,8,9,10,11,12,13,-3,-2, 0,1, 2, 3]
    print(find_min(nums))
