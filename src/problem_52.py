#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import copy
class Solution0:
    """
    借鉴Disscusion中的答案
    核心：
        用一维列表记录每一行放置的列索引就好！，不用存储整个二维列表！下标i代表行，chessboard[i]中存储
    的代表列！具体参见51题题解
    """
    def __init__(self):
        self.res = 0

    def totalNQueens(self, n):
        def valid(chessboard, row):
            for i in range(row):
                if chessboard[i] == chessboard[row] or abs(chessboard[row] - chessboard[i]) == row - i:
                    return False
            return True

        def dfs(chessboard, row):
            if row == n:
                self.res += 1
                return
            for col in range(n):
                chessboard[row] = col  # 第row行放在第col列上
                if valid(chessboard, row):
                    dfs(chessboard, row + 1)

        dfs([-1] * n, 0)
        return self.res
class Solution:
    def __init__(self):
        self.result = 0

    def totalNQueens(self, n):
        """
        My method
            类似于51题N-Queens中我的解法，时间复杂度挺高的
        """
        def putQueen(row, col, chessboard):
            chessboard[row][col] = 'Q'
            for i in range(row, n):
                for j in range(n):
                    if (i == row or j == col or abs(i - row) == abs(j - col)) and chessboard[i][j] == '.':
                        chessboard[i][j] = 'x'
            return chessboard

        def generate(row, chessboard):
            if row > n - 1:
                return
            for col in range(n):
                if chessboard[row][col] == '.':
                    chess = putQueen(row, col, copy.deepcopy(chessboard))
                    if row == n - 1:
                        self.result += 1
                    generate(row + 1, copy.deepcopy(chess))

        chessboard = [['.' for i in range(n)] for j in range(n)]
        generate(0, chessboard)
        return self.result
