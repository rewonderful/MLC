#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def search0( nums, target):
    """
    算法：二分查找
    思路：
        区间形式：
            ____↗️____|___↗️____
        把lo = mid + 1看做是选择右半段查找，hi = mid - 1看作是选择左半段查找
        即每次查找分割的时候，选择
            左:hi = mid - 1
            右:lo = mid + 1
            把区间分成递增区间和旋转区间，递增区间就是有序的区间如[1,2,3]，旋转区间就是包含一段
        有序和另外一段有序的混合区间[5,6,7,1,2,3]
            查找一个数字target时，target与nums[mid]的关系只有相等，小于，大于，分别对应三种处理
        相等时返回，没的说，小于或者大于的时候，target，mid一定不是位于递增区间，就是位于旋转区间，
        或者说 mid 左侧是旋转区间or递增区间，mid右侧是旋转区间or递增区间
            则可以形式化算法为：
            if target < nums[mid]:
                [lo__target___↗️__]mid[__|___↗️____hi]
                if target >= nums[lo]，即mid左侧是递增区间，target在递增区间内（nums[lo]<=target<nums[mid]）：
                    在左侧查找target
                [lo___↗️__]mid[__|___↗️___target__hi]
                else 说明target 在右侧旋转区间：
                    右侧查找
                [lo____↗️___|__target__]mid[___↗️____hi]
                if  mid 左边是旋转区间，则右侧是递增区间，而taget<nums[mid],一定不去右边找
                    左侧查找，
            else 说明 target > nums[mid]
                [lo____↗️____|__]mid[__target___↗️____hi]
                if target <= nums[hi] ,即target在递增区间(nums[mid]<=target<nums[hi])
                    在右侧递增区间查找
                [lo____↗️__target___|__]mid[___↗️____hi]
                else target不在右侧递增区间内：
                    在左侧旋转区间查找
                [lo____↗️___]mid[__target___|___↗️____hi]
                if mid左边是递增区间，右侧是旋转区间，而target>nums[mid],则一定不去左边找
                    右边查找
    复杂度分析：
        时间：OlogN，二分查找logN
        空间：O1，常数级
    """
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (hi+lo) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            if nums[lo] <= target or nums[mid] < nums[lo]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[hi] >= target or nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
def search1(self, nums, target):
    """
    算法：暴力遍历
    思路：遍历一遍数组看有没有
    复杂度分析：
        时间：ON，遍历一遍数组
        空间：O1，常数级
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def search2(self, nums, target):
    """
    算法：移位二分
    思路：
            现在的列表是两端递增有序列表拼接而成，根据target大小的情况挪动lo或者hi，将lo，hi固定在一个
        正常递增的区间内再二分查找
    复杂度分析：
        时间：OlogN~ON，挪lo，hi比较费时间，差一点的情况可能要ON
        空间：O1，常数级
    """
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        if target < nums[lo] and nums[lo] > nums[hi]:
            lo += 1
        if target > nums[hi] and nums[lo] > nums[hi]:
            hi -= 1
        if nums[lo] <= nums[hi]:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
    return -1

if __name__ == '__main__':
    print(search0([4,5,6,7,8,1,2,3],8))