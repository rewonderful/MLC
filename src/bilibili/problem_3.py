#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def solution(p,s,n):
    if s > sum(p):
        return -1
    i,j = 0,0
    ans = float('inf')
    count = p[0]
    while i <n and j < n:
        if count >= s and j-i+1 < ans:
            ans = j-i+1
        if count >= s and i < n - 1:
            count -= p[i]
            i += 1
            continue
        if count < s and j < n - 1:
            j += 1
            count += p[j]
            continue

        break

    return ans


if __name__ == '__main__':
    # n = 5
    # s = 7
    # p = [1, 2, 3, 4, 5]
    n,s = list(map(int,input().strip().split(" ")))
    p = list(map(int,input().strip().split(' ')))
    print(solution(p,s,n))
