#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import random
def quick_sort(arr, left, right):
    # 只有left < right 排序
    if left >=right:
        return
    #在列表里随机选一个数来作为基准元素
    random_index = random.randint(left, right)
    #把基准元素和第一个元素交换
    arr[left], arr[random_index] = arr[random_index], arr[left]
    pivot = arr[left]
    #定义lt：小于v部分元素 的【下标】，初始是空的，因为arr[left]是基准元素
    lt = left # arr[left+1...lt] < v
    #gt 大于v 部分开始的【下标】，初始为空
    gt = right + 1 # arr[gt...right] > v
    i = left + 1 # arr[lt+1...i] == v
    #终止条件：下标i 和gt 遇到一起，说明都排完了
    while i < gt:
        if arr[i] < pivot:
            arr[i], arr[lt+1] = arr[lt+1], arr[i] #将小于v的元素下标后移
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt-1] = arr[gt-1], arr[i]  #将大于v的元素下标前移
            gt -= 1
        else:
            i += 1
     #最后把第一个元素（基准元素）放到等于v的部分
    arr[left], arr[lt] = arr[lt], arr[left]
    #递归排序
    quick_sort(arr, left, lt-1)
    quick_sort(arr, gt, right)

if __name__ == '__main__':
    n = 50000
    print("BEFORE")
    nums = [ random.randrange(n) for _ in range(n//2)]
    print(nums)
    quick_sort(nums,0,len(nums)-1)
    print('AFTER')
    print(nums)