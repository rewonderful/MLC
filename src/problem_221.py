#!/usr/bin/env python
def maximalSquare(self, matrix):
    """
    My Method
    算法：动规
    思路：
        用dp[i][j]记录以matrix[i][j]为"1"矩形的右下角的矩形的最大边长
        matrix[i][j] == 0 的显然dp[i][j] == 0
        对matrix[i][j] == 1的来说，如果在第一行或者第一列，显然dp[i][j]=1，最大也就是这么大了
        对于其他位置，
        像下面这样，右下角的那个1称之为matrix[i][j]，那么要检查它的左，上，左上三个位置是否都为1，
        如果这三个位置有一个不为1的，那么显然以i,j为最大矩形的右下角的那个矩形，只能是matrix[i][j]本身
        那么dp[i][j] =1
        否则就要看这三个位置的dp情况,可以看到，如果右下角的i,j代表的那个矩形，如果想扩充边长的话，其
        值应该是dp[i][j] = min(dp[左],dp[上],dp[左上])+1,如此便可以构建状态转移方程
            1 1         1 1 1       0 1 1
            1 1   -->   1 1 1  vs   1 1 1
                        1 1 1       1 1 1
    """
    if matrix == [] or matrix[0] == []:
        return 0
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = int(matrix[i][j])
            elif matrix[i][j] == '1':
                if matrix[i - 1][j - 1] == '1' and matrix[i][j - 1] == '1' and matrix[i - 1][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                else:
                    dp[i][j] = 1
            else:
                dp[i][j] = 0
            ans = max(ans, dp[i][j])
    return ans ** 2

def maximalSquare1(self, matrix):
    """
    Solution Method
    事实上，在状态转移时，可以不用管上下左右是不是'1'，如果不是1的话，那么最小值就是0，当前值就是0+1 = 1
    0 1
    1 1
    其实就是把我冗余的判断精简了
    """
    if matrix == [] or matrix[0] == []:
        return 0
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = int(matrix[i][j])
            elif matrix[i][j] == '1':
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
            else:
                dp[i][j] = 0
            ans = max(ans, dp[i][j])
    return ans ** 2
if __name__ == '__main__':
    print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))