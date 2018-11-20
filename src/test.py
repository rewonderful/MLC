#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def chinese(data):
    count = 0
    for s in data:
        if ord(s) > 127:
            count += 1
    return count

def singleNumber( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums)):
        if nums[i] not in nums[i + 1:]:
            return nums[i]
if __name__ == '__main__':
    print(singleNumber([2,2,1]))




