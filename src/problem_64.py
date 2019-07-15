#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def minPathSum0( grid):
    """

    直接用grid就好，没有必要再新建一个dp数组了
    因为遍历顺序反正也是一行一行的，且直接用grid，先后顺序也不影响。前面的值即使原地改变了，对后面也没影响的
    """
    if not grid:
        return 0
    m = len(grid)
    n = len(grid[0])
    for i in range(1, m):
        grid[i][0] += grid[i - 1][0]
    for j in range(1, n):
        grid[0][j] += grid[0][j - 1]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    return grid[-1][-1]
def minPathSum(self, grid):
    """
    My Method
    算法：递归/自底向上
    思路：
        首先很好想到用动规做。当前位置dp[i][j]与子状态dp[i][j+1],dp[i+1][j]的关系就是
        dp[i][j] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
        如果知道哪个子问题最小，那么就走下方dp[i+1][j]或者右方dp[i][j+1]。并且最小值等于它的
        值+ grid[i][j]

        用自底向上的思路，边界条件即右下角的值为边界条件，dp[-1][-1] = 1
    复杂度分析：
        时间：OMN，遍历M行N列所有位置
        空间：OMN，dp数组的大小
    """
    if grid == []:
        return 0
    m = len(grid)
    n = len(grid[0])
    dp = [[float('inf') for _ in range(n)] for _ in range(m)]
    dp[m - 1][n - 1] = grid[m - 1][n - 1]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                continue
            if i == m - 1:
                dp[i][j] = dp[i][j + 1] + grid[i][j]
            if j == n - 1:
                dp[i][j] = dp[i + 1][j] + grid[i][j]
            if i < m - 1 and j < n - 1:
                dp[i][j] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
    return dp[0][0]

def minPathSum1(self, grid):
    """
    算法：动规/自顶向下
    思路：
        和自底向上一样，这里换成了自顶向下
    复杂度同自底向上
    """
    if grid == []:
        return 0
    m = len(grid)
    n = len(grid[0])
    dp = [[float('inf') for _ in range(n)] for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i == 0:
                dp[i][j] = dp[i][j - 1] + grid[i][j]
            if j == 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
    return dp[-1][-1]