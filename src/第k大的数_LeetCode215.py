#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findKthLargest( nums, k):
    """

    快排的思想
    根据pivot将左右两侧划分，在划分后就可以得到p，将p和k比较，如果k在p的左侧，那么就丢弃右侧，只排序左侧，如果k在右侧，那么就
    丢弃左侧，只排序右侧，
        要注意这里的partition一次排序是从大到小排
        注意第k大，所以要 p+1
        注意find_kth中的while是l<=r，有等于号
    复杂度：On
    """
    def partition(nums, l, r):
        pivot = nums[l]
        while l < r:
            while l < r and nums[r] <= pivot:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] > pivot:
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        return l

    def find_kth(nums, l, r):
        while l <= r:
            p = partition(nums, l, r)
            if p + 1 == k:
                return nums[p]
            elif k < p + 1:
                r = p - 1
            else:
                l = p + 1

    return find_kth(nums, 0, len(nums) - 1)