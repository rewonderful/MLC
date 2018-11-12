#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def singleNumber(self, nums):
    """
    算法：
        利用异或运算的特性来【去重】，最后剩下的就是单个数字
        Python中异或：
            N^0 = N
            N^N = 0
            A^B^A = (A^A)^B = 0^B = B
    复杂度分析：
        时间：On 遍历一次数组
        空间：O1 额外的bit存储结果
    """
    bit = 0
    for num in nums:
        bit ^= num
    return bit