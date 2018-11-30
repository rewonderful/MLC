#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def merge(nums):

    if len(nums) < 2:
        return nums
    mid = len(nums)//2
    leftpart = merge(nums[:mid])
    rightpart = merge(nums[mid:])

    return  mergesort(leftpart,rightpart)
def mergesort(left,right):
    result = []
    i = 0
    j = 0
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])
    return result
if __name__ == '__main__':
    print(merge([9,8,7,6,5,4,3,2,1,0]))
    #print(mergesort([1,5,7],[2,4,6]))