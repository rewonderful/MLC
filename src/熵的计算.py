#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from math import log
def H (p):
    h = 0
    for item in p :
        h += - item * log(item)
    return h
if __name__ == '__main__':
    print(H([0.5,0.5]))
    print(H([0.1,0.9]))
