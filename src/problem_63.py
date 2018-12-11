#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def uniquePathsWithObstacles(self, obstacleGrid):
    """
    算法：动规
    思路：
        和62题基本一样

        dp[i][j] 记录当前位置ij到达右下角有几种不同的方式
        状态转移方程：
        中间位置i,j
         if obstacleGrid[i][j] == 1：
            dp[i][j] = 0
        else:
            dp[i][j] = dp[右侧]+dp[下侧]
        如果在最后一行或者最后一列，其实和中间位置是一样的，只不过因为在边界，只考虑一侧以及obstacleGrid[i][j] == 1

        边界条件：
            dp[最末端位置] = 1
    复杂度分析：
        时间：ON2，两层for
        空间：ON2，dp数组空间
    """
    if obstacleGrid == [] or obstacleGrid[-1][-1] == 1:
        return 0
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[0] * n for _ in range(m)]
    dp[-1][-1] = 1
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                continue
            if i == m - 1:
                dp[i][j] = dp[i][j + 1] if obstacleGrid[i][j] != 1 else 0
            elif j == n - 1:
                dp[i][j] = dp[i + 1][j] if obstacleGrid[i][j] != 1 else 0
            else:
                dp[i][j] = dp[i][j + 1] + dp[i + 1][j] if obstacleGrid[i][j] != 1 else 0
    return dp[0][0]