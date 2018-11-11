#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def reverse(x):

    x = int('-'+str(abs(x))[::-1]) if x < 0 else int(str(x)[::-1])

    return 0 if x< -pow(2,32) or x >=pow(2,32) else x
if __name__ == '__main__':
    x=-123
    print(reverse(x))