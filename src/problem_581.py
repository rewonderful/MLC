#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findUnsortedSubarray(self, nums):
    """
    Method 2
    栈
    相当于是用单调栈
    第一次用升序单调栈，栈内存储的元素是升序的，然后遍历数组内元素，找到不符合升序位置的元素，
    最小的其在排序数组中应该在的位置
    第二次用降序单调栈，栈内存储的元素是降序的，倒着遍历数组内元素，找到不符合降序位置的元素，
    最大的其在排序数组中应该在的位置

    二者只差就是目标解

    不过也可能 r - l < 0,标志着数组本身就是有序的，return 0
    """
    stack = []
    l, r = len(nums), 0
    for i in range(len(nums)):
        while stack and nums[stack[-1]] > nums[i]:
            l = min(l, stack.pop())
        stack.append(i)
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[stack[-1]] < nums[i]:
            r = max(r, stack.pop())
        stack.append(i)
    if r - l >= 0:
        return r - l + 1
    else:
        return 0

def findUnsortedSubarray1(self, nums):
    """
    Method 1
    Sort
    将数组拷贝后排序，然后看看元素不一致的起止位置
    """
    nums_copy = nums[:]
    nums_copy.sort()
    start, end = len(nums), -1
    for i in range(len(nums)):
        if nums_copy[i] != nums[i]:
            start = min(start, i)
            end = max(end, i)
    if end - start >= 0:
        return end - start + 1
    else:
        return 0
if __name__ == '__main__':
    print(findUnsortedSubarray([1,3,8,2,6,3,5,9]))