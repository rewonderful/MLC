#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def LongestCommonSubsequence(s1,s2):

    if s1 == '' or s2 =='':
        return 0
    m , n= len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    dp[0][0] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return dp[-1][-1]

if __name__ == '__main__':
    #print(LongestCommonSubsequence('ABCBDAB','BDCABA'))
    print(LongestCommonSubsequence('ABCD','EACB'))