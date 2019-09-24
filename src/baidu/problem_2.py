#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def solution(nums,n):
    dp = nums + [0]*(n+1-4)
    for i in range(5,n+1):
        dp[i] = dp[i-1]+dp[i-3]+dp[i-4]
    return dp[n]

if __name__ == '__main__':
    a1,a2,a3,a4,n = list(map(int,input().strip().split(" ")))
    nums = [0,a1,a2,a3,a4]
    # nums = [0,1,2,3,4]
    # n = 20
    print(solution(nums,n))