#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def LongestCommonSubstring(s1,s2):
    """
    这里的dp[i][j]的含义变成了以i，j结尾的最长子串
    如果还是和子序列同等含义的话，比如ABC D F 和ABC E F，在最后的F处都会dp[i-1][j-1] + 1，然后错误判断为最长是5

    """
    ans = 0
    if s1 == '' or s2 =='':
        return 0
    m , n= len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    dp[0][0] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                ans = max(ans,dp[i][j])
    return ans

if __name__ == '__main__':
    #print(LongestCommonSubsequence('ABCBDAB','BDCABA'))


    print(LongestCommonSubstring('asdfas','werasdfaswer'))