#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def isPalindrome( x: int) -> bool:
    if x < 0:
        return False
    else:
        div = 1
        while x // div >= 10:
            div *= 10
        while x > 0:
            first = x // div
            last = x % 10
            if first != last:
                return False
            x = (x % div) // 10
            div //= 100
        return True
def isPalindrome0(x):
    if x < 0:
        return False
    else:
        return str(x)==str(x)[::-1]

if __name__ == '__main__':
    x=121
    print(isPalindrome(x))

