#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import random

"""
快排第一种方式
"""
def partition(nums,l,r):
    """
    一次分割位置，
    将nums[l]的值作为pivot作为支点进行左右挪腾，因为取的是左侧为支点，所以先从右边大于pivot的位置进行调换处理

    遍历右侧，找到小于pivot的位置的值，和左侧nums[l]进行调换
    遍历左侧，找到大于等于pivot的位置的值，和右侧的nums[r]进行调换

    可以直接进行
        nums[l],nums[r] = nums[r],nums[l]
        这样的调换，因为一开始pivot = nums[l]，所以最后nums[l]的值就是pivot，不用单独设置nums[l] = pivot
    但是如果
        只是nums[l] = nums[r]这样赋值的话，后面还是需要单独nums[l] = pivot赋值一下的
    """
    pivot = nums[l]
    while l < r :
        while nums[r] >= pivot and r > l:
            r -= 1
        nums[l] = nums[r] #or  nums[l],nums[r] = nums[r],nums[l]
        while nums[l] < pivot and r > l:
            l += 1
        nums[r] = nums[l] ##or  nums[l],nums[r] = nums[r],nums[l]
    nums[l] = pivot #最后nums[l]的位置的值就是pivot
    return l
def quick_sort(nums,lo,hi):
    """
    "主"排序代码
    作为排序的入口，对当前nums进行分割调整，调整后对左侧调整，再对右侧调整，这样的话是比较清晰
    这里也要有lo和hi，来定义对数组的哪部分区间进行调整，因为递归过程中hi和lo会改变，所以要加上先定条件lo < hi
    快排是原地排序，不需要return nums
    """
    if lo < hi :
        p = partition(nums,lo,hi)
        quick_sort(nums,lo,p-1)
        quick_sort(nums,p+1,hi)
    return
"""
快排第二种，默写出来的要！
"""
def quick_sort2(nums,lo,hi):
    if lo < hi:
        l = lo
        r = hi
        pivot = nums[l]
        while l < r :
            while nums[r] >= pivot and r > l:
                r -= 1
            nums[l] = nums[r]
            while nums[l] < pivot and r > l:
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        quick_sort2(nums,lo,l-1)
        quick_sort2(nums,l+1,hi)
"""
算法导论上的写法
"""
def partition3(nums,lo,hi):
    """
    以最右侧的元素为支点，遍历lo到hi 之间，一遍for
    i记录的是从前往后最后一个小于等于pivot的位置,那么i+1后就是第一个大于pivot的位置
    所以从左往右遍历如果当前nums[j] <=pivot就后挪j，
        并且将nums[i]和nums[j]调换，确保从0到i的下标记录的值都是小于等于pivot的
        比如[9,2,3,5,2],就需要nums[i]和nums[j]调换-->[2,9,...]
    最后将nums[i]+1和nums[hi]交换位置
    可以手推一下-->[3,4,6,9,7,4,8,5]
    """
    pivot = nums[hi]
    i = lo - 1
    for j in range(lo,hi):
        if nums[j] <= pivot:
            i += 1
            nums[i],nums[j] = nums[j],nums[i]
    nums[i+1],nums[hi] = nums[hi],nums[i+1]
    return i + 1

def quick_sort3(nums,lo,hi):
    if lo < hi:
        p = partition3(nums,lo,hi)
        quick_sort3(nums,lo,p-1)
        quick_sort3(nums,p+1,hi)
    return
"""
"""
def quick_sort4(nums, l, r):
    """
        非递归的写法，其实就是用一个队列或者栈来保存l和r，其实可以联想一下，本来计算机中函数递归就会有递归栈来保存函数的状态，
    参数等，只不过现在人为地用栈来保存罢了，注意这里其实用stack和queue都可以，因为对一个待排序列的左半部分先排序还是右半部分
    先排序，是不要紧的
    """
    if l >= r:
        return
    stack = []
    stack.append((l,r))
    while stack:
        pair = stack.pop()
        lo = pair[0]
        hi = pair[1]
        if hi  <=  lo:
            continue
        #这部分其实就是前面的各种patition部分
        # pivot = nums[hi]
        # i = lo - 1
        # for j in range(lo, hi):
        #     if nums[j] <= pivot:
        #         i += 1
        #         nums[i], nums[j] = nums[j], nums[i]
        # nums[i + 1], nums[hi] = nums[hi], nums[i + 1]
        # p = i+ 1
        #-----------------------------------------
        l = lo
        r = hi
        pivot = nums[l]
        while l < r:
            while nums[r] >= pivot and r > l:
                r -= 1
            nums[l] = nums[r]
            while nums[l] < pivot and r > l:
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        p = l


        stack.append((lo, p - 1))
        stack.append((p + 1, hi))



def quick_sort7(nums,l,r):
    if l < r:
        p = partition_7(nums,l,r)
        quick_sort7(nums,l,p-1)
        quick_sort7(nums,p+1,r)
def partition_7(nums,l,r):
    pivot = nums[l]
    while l < r :
        while l < r and nums[r] >= pivot:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] < pivot:
            l += 1
        nums[r] = nums[l]
    nums[l] = pivot
    return l

if __name__ == '__main__':
    n = 50
    print("BEFORE")
    nums = [ random.randrange(n) for _ in range(n//2)]
    print(nums)
    quick_sort4(nums,0,len(nums)-1)
    print('AFTER')
    print(nums)
