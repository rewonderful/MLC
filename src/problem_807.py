#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def maxIncreaseKeepingSkyline(self, grid):
    """
    每一行最大值算出来。每一列最大值算出来，然后累加 ans += min(row_i,col_j)-val
    注意这里用zip(*grid)来转换grid的行列
    """
    row_maxes = [max(row) for row in grid]
    col_maxes = [max(col) for col in zip(*grid)]
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            ans += min(row_maxes[i], col_maxes[j]) - grid[i][j]
    return ans