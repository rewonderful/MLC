#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def numSquares( n):
    """
    算法：动规
    思路：
        其实这个方法TLE了，但是Java写就Ok，所以很迷，case也都对
        所以就记录一下思路吧，很明显的递归题
        状态转移方程是
            当前的i取决于所有小于i的平方和组合的最小的计数
            dp[13]
                13 = 3**2+ 4
                13 = 2**2 + 9
                13 = 1**2 + 12
            那么dp[13] = min(dp[4],dp[9],dp[12])+1

            dp[i] = min(dp[i],dp[i-j*j]+1)
            这里不用for j in range来确定j的固定取值范围是有好处的，要不还得math.sqrt(i)或者i//2来确定
            直接用while i-j*j，然后j+=1就OK了，最贴切本题
    """
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, len(dp)):
        j = 1
        while i-j*j >=0:
            dp[i] = min(dp[i],dp[i-j*j]+1)
            j += 1
    return dp[-1]
if __name__ == '__main__':
    print(numSquares(7216))