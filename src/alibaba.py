#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# def solution(p):
#     ans = 0
#     return ans
# if __name__ == '__main__':
#     N = int(input().strip(' '))
#     p = []
#     for _ in range(N):
#         p.append(eval(input().strip(' ')))
#     print(solution(p))
# def solution(m,n,k):
#     if k == 1 :
#         return 0
#     if k == 2:
#         return 1
#     dp = [[0] * (k + 1) for _ in range(m + 1)]
#
#     for i in range(m + 1):
#         dp[i][0] = 0
#         dp[i][1] = 1
#     for j in range(k + 1):
#         dp[0][j] = 0
#
#     for i in range(1,m + 1):
#         for j in range(k + 1):
#             if i < j:
#                 dp[i][j] = dp[i][j-1]
#             else:
#                 dp[i][j] = dp[i][j-1]+dp[i-j][j]
#     return dp[m][k]
def solution( m,n, k):
    if k == 1:
        return 0
    if k == 2:
        return 1
    dp_m = [[0] * (k + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp_m[i][1] = 1
    for j in range(k + 1):
        dp_m[0][j] = 1
    for i in range(1, m + 1):
        for j in range(1, k + 1):
            if i < j:
                dp_m[i][j] = dp_m[i][i]
            else:
                dp_m[i][j] = dp_m[i][j - 1] + dp_m[i - j][j]

    dp_n = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp_n[i][1] = 1
    for j in range(k + 1):
        dp_n[0][j] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i < j:
                dp_n[i][j] = dp_n[i][i]
            else:
                dp_n[i][j] = dp_n[i][j - 1] + dp_n[i - j][j]

    ans = 0
    for  i in range(1,k):
        ans += (dp_m[m][i] * dp_n[n][k-i])%10000
        ans = ans%10000

    return ans

if __name__ == '__main__':
    # m = int(input().strip(' '))
    # n = int(input().strip(' '))
    # k = int(input().strip(' '))
    # print(solution(m,n,k))
    print(solution(1,1, 3))