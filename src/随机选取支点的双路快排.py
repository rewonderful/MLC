#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import random
def _partition_doubule(arr, l, r):
    ind = random.randint(l, r)
    arr[l], arr[ind] = arr[ind], arr[l]
    stand = arr[l]
    i, j = l + 1, r
    while True:
        while i <= r and arr[i] < stand:  # 不能改为arr[i] <= stand, 原因下文有讲解
            i += 1
        while j >= l + 1 and arr[j] > stand:  # 不能改为arr[j] >= stand.
            j -= 1
        if i > j:
            break
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    arr[j], arr[l] = arr[l], arr[j]
    return j


def _quick_sort(arr, l, r):
    p = _partition_doubule(arr, l, r)
    _quick_sort(arr, l, p - 1)
    _quick_sort(arr, p + 1, r)



