#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def f (x):
    #return 2*pow(x,3)-15*pow(x,2)-36*x+7-37
    return 2*x*x - 4
def df(x):
    #return 6*pow(x,2)-30*x-36
    return 4 * x

def iteration(x):
    return x - f(x)/df(x)


if __name__ == '__main__':

    x0 = 1
    epsilon = 1e-5
    iter = 0

    while iter < 1000:
        x = iteration(x0)
        if abs(x - x0) < epsilon:
            break
        else:
            x0 = x
        iter += 1
    print(x0)


