#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def solution(a,b):
    lo = 0
    hi = a
    # mid = ((lo+hi)/2)**b
    # while (mid - a) > 1e-7:
    #     if mid >
    while lo <= hi:
        mid = (lo+hi)/2

        if mid**b == a or abs(mid**b - a) <=1e-9:

            return  round(mid,6)
        elif mid**b > a:
            hi = mid
        else:
            lo = mid
    #return mid



if __name__ == '__main__':
    a,b = list(map(int,input().strip().split(" ")))
    #print(solution(1000,2))
