#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def solution(x):
    lo = 0
    hi = x if x > 1 else 1
    eps = 1e-10

    while lo <= hi:
        mid = (lo+hi)/2
        if abs(mid**2 - x) < eps:
            return mid
        elif mid **2 > x:
            hi = mid
        else:
            lo = mid

def newton(n):
    def f(x):
        return x ** 2 - n
    def df(x):
        return 2*x
    def iteration(x):
        return x - f(x)/df(x)

    iter = 0
    x0 = -0.1
    while iter < 1000:
        x = iteration(x0)
        if abs(x-x0) < 1e-5:
            break
        else:
            x0 = x
        iter += 1

    return x0

if __name__ == '__main__':
    print(newton(100))