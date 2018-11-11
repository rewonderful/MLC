#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def addBinary( a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    num = int(a, 2) + int(b, 2)
    ans = bin(num)
    return ans[2:]
if __name__ == '__main__':
    a = '1101'
    b = '10'
    print(addBinary(a,b))