#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def isPowerOfTwo( n):
    """
    算法：
        使用位运算，n与n-1进行位与&操作，所有2的power表示成二进制都只有首位一个1（即10000，n-1为01111），位与之后为0。
    复杂度分析：
        时间： O1
        空间： O1
    """
    if n <= 0:
        return False
    return True if n & (n - 1) == 0 else False
