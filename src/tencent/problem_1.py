#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import heapq
def solution(A,B):

    ans = []
    min_b = min(B)
    max_b = max(B)
    for a in A:
        ans.append(max(a*max_b,a*min_b))

    ans.sort(reverse=True)
    return ans[1]





if __name__ == '__main__':
    n, m = list(map(int,input().strip().split()))
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))

    # n, m = 2,2
    # A = [20,18]
    # B = [2,14]

    print(solution(A,B))
