#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def solution(n):
    if n  == 0 or n == 2:
        return 1

    dp = [0]*(n+1)
    dp[0] = 1
    dp[2] = 1
    for i in range(4,n+1,2):
        for j in range(1,i):
            dp[i] += (dp[j-1] * dp[i-1-j]) #dp[i-2] * 2 + dp[(i-2)//2] ** 2
    return dp[n]%100007

if __name__ == '__main__':
    #n = int(input().strip())
    n = 6
    print(solution(n))
