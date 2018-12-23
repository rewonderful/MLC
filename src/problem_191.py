#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def hammingWeight(self, n):
    """
    像十进制下每次除以10一位一位取出来数一样，取末尾的值，然后右移
    """
    counter = 0
    while n != 0:
        counter += (n & 1)
        n >>= 1
    return counter