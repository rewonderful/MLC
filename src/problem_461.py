#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def hammingDistance(self, x, y):
    """
    算法：bit操作
    思路：
        首先很容易想到用异或x^y来求得x和y不同位置的"情况"，
        1    (0 0 0 1)
        4    (0 1 0 0)
       异或->   1 0 1
        剩下的问题就是数有几个1了，可以像十进制下每次除以10一位一位取出来数一样，取末尾的值，然后右移
    复杂度分析：
        时间：ON
        空间： O1
    """
    num = x ^ y
    counter = 0
    while num != 0:
        counter += (num & 1)
        num >>= 1
    return counter