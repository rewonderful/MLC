#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def twoSum(self, numbers, target):
    """
    数组已经排序过了，夹逼去靠近target就好
    """
    left = 0
    right = len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1

def twoSum_(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    record = {}
    for i in range(len(numbers)):
        if numbers[i] in record:
            return [record[numbers[i]] + 1, i + 1]
        else:
            record[target - numbers[i]] = i
