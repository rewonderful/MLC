#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def recursion(n):
    if n == 0:
        return 1
    else:
        return n*recursion(n-1)

if __name__ == '__main__':
    print(recursion(4))
    max()