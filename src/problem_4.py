#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findMedianSortedArrays0( nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    len_nums = len(nums)
    if len_nums % 2 == 0:
        mid1 = nums[int(len_nums / 2)]
        mid2 = nums[int(len_nums / 2) - 1]
        return (mid1 + mid2) / 2
    else:
        return nums[int(len_nums / 2)]
def findMedianSortedArrays( nums1, nums2):
    len1 = len(nums1)
    len2 = len(nums2)
    if len1 == 0 or len2 == 0 or nums1[0] >= nums2[-1] or nums2[0] >=nums1[-1] :
        nums = nums1 + nums2
        len_nums = len(nums)
        if len_nums % 2 == 0:
            mid1 = nums[int(len_nums / 2)]
            mid2 = nums[int(len_nums / 2)-1]
            return (mid1 + mid2) / 2
        else:
            return nums[int(len_nums/2)]
    else:
        len_total = len1 + len2
        if len_total % 2 == 0:
            mid1 = len_total/2
            mid2 = mid1-1



if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [4,5,6]
    mid = findMedianSortedArrays(nums1,nums2)
    print(mid)