#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def uniquePaths( m, n):
    """
    算法：动规
    思路：
        dp[i][j] 记录当前位置ij到达右下角有几种不同的方式
        状态转移方程：
            dp[i][j] = dp[右侧]+dp[下侧]
        边界条件：
            dp[最后一行] = 1
            dp[最后一列] = 1
            dp[最末端位置] = 1
    复杂度分析：
        时间：ON2，两层for
        空间：ON2，dp数组空间
    """
    dp = [[0] * n for _ in range(m)]
    dp[-1][-1] = 1
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                continue
            if i == m - 1 or j == n - 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
    return dp[0][0]
if __name__ == '__main__':
    print(uniquePaths(4,3))