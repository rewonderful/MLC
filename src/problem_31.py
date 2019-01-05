#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def nextPermutation(self, nums):
    """
    My Method
    算法：指针+快排
    思路：
        首先要理解题意，这个有点头疼，把题意理解后拆分成两个部分就好做了。

        题目要求的是下一个更大的排列数，如果没有下一个更大的排列数的话，就将序列升序排序
       [1,2,3,5,6,4,3] --> 1,2,{4,3,3,5,6}
        就是找到下一个更大的数
        所以我就从后向前，找到第一个出现拐点不是升序排序的两个下标，即上面这个例子中的3和5，
        然后再从3往后的部分中找到最小的大于3的数字的下标，并且交换这两个位置的值，那么就是4
        所以我这里有两层while套着，第一层外面的while是去找到nums[l]<nums[r]的位置，第二层
        从l到len(nums-1)找到最小的大于nums[l]的数的下标min_max_index，然后交换l和min_max_index
        的值，退出
        此时的nums[l+1:]指向的就是待排的剩余序列，用快排排序即可，并且如果整个序列是升序的，那么退出while
        的条件就是l = -1,此时就是对l+1=0开始对整个数组排序
        所以这个题其实就是两个步骤：
            1.调整
            2.排序
    """
    if len(nums) < 2:
        return
    r = len(nums) - 1
    l = len(nums) - 2
    while l >= 0:
        if nums[l] >= nums[r]:
            r = l
            l -= 1
        elif nums[l] < nums[r]:
            min_max_index = len(nums) - 1
            while min_max_index > l:
                if nums[min_max_index] > nums[l]:
                    break
                min_max_index -= 1
            nums[l], nums[min_max_index] = nums[min_max_index], nums[l]
            break
    def partition(nums, lo, hi):
        if lo > hi:
            return
        pivot = nums[lo]
        l = lo
        r = hi
        while l < r:
            while l < r and nums[r] >= pivot:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] < pivot:
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        return l

    def quick_sort(nums, lo, hi):
        if lo < hi:
            p = partition(nums, lo, hi)
            quick_sort(nums, lo, p - 1)
            quick_sort(nums, p + 1, hi)

    quick_sort(nums, l+1, len(nums) - 1)

def nextPermutation1(self, nums):
    """
    Solution Method
    算法：指针+交换调整
    思路：
        整体来说和上面的 My Method一样，不同的是这里第二步排序的时候，利用了经过第一步调整后后序序列一定是
        降序排序的特征进行调换元素的方式进行排序处理，比快排要快
        所以还是要根据题目特征去调整的，不能简单粗暴就上快排
    """
    if len(nums) < 2:
        return
    r = len(nums) - 1
    l = len(nums) - 2
    while l >= 0:
        if nums[l] >= nums[r]:
            r = l
            l -= 1
        elif nums[l] < nums[r]:
            min_max_index = len(nums) - 1
            while min_max_index > l:
                if nums[min_max_index] > nums[l]:
                    break
                min_max_index -= 1
            nums[l], nums[min_max_index] = nums[min_max_index], nums[l]
            break
    lo = l + 1
    hi = len(nums) - 1
    #swap
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1