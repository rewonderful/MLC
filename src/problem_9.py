#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def isPalindrome(x):
    if x < 0:
        return False
    else:
        return str(x)==str(x)[::-1]

if __name__ == '__main__':
    x=10
    print(isPalindrome(x))

