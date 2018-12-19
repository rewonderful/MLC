#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def moveZeroes( nums):
    """
    算法：UM。。
    思路：
        zero记录第一个0元素的位置，将非0元素和第一个0元素调换位置
    复杂度分析：
        时间：ON,
        空间：O1
    """
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
def moveZeroes1(self, nums):
    """
    算法：UM。。
    思路：
        设置index记录非0元素的位置，从0开始，遍历nums，将nums[index]值赋值为非0的nums[i]
    复杂度分析：
        时间：ON,
        空间：O1
    """
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    nums[index:] = [0] * (len(nums) - index)
def moveZeroes2( nums):
    """
    算法："冒泡排序"
    思路：
        将0一个个的冒泡到后面去，或者说将非0元素一个个冒到前面来，并且调换位置后直接break
    复杂度分析：
        时间：ON2，最差要ON2，
        空间：O1
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                break
if __name__ == '__main__':
    print(moveZeroes([0,1,0,3,12]))