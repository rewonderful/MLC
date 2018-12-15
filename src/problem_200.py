#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def numIslands(self, grid):
    """
    My Inital Method
    算法：深度优先搜索
    思路：
        理解题意，岛屿数量就是有多少个由1连通的区域，其中连通的定义是在上下左右4个方向上裁定
        故遍历二维数组。从土地1开始进行深度优先搜索，建立一个visit辅助二维表标记该位置是否访问过，
        要注意判断上下左右4个方向是否合法再进行探索
        在外面for for 能进行几次，就说明有几个连通的1构成岛屿
    复杂度分析：
        时间：ON2吧应该是
        空间：ON2，visit列表和递归栈
    """
    if grid == []:
        return 0
    m = len(grid)
    n = len(grid[0])

    visit = [[0] * n for _ in range(m)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def check_legal(x, y):
        return x >= 0 and x <= m - 1 and y >= 0 and y <= n - 1 and grid[x][y] == '1' and visit[x][y] == 0

    def dfs(i, j):
        visit[i][j] = 1
        for x_delta, y_delta in direction:
            x, y = i + x_delta, j + y_delta
            if check_legal(x, y):
                dfs(x, y)

    counter = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and visit[i][j] == 0:
                dfs(i, j)
                counter += 1
    return counter

def numIslands1(self, grid):
    """
    Disscussion Method
    主题思路是和My Method的一样的
    也是深搜
    但是这里有趣的是，它不用设立visit列表，二是将与1连通的其他1，都标记为0，陆地变海洋，将连通的1
    融化为1个1，然后for循环看最后剩下几个1就说明是彼此不连通的区域，即为解
    """

    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

    num_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                num_islands += 1
                dfs(i, j)
    return num_islands

def numIslands2(self, grid):
    """
    My Upper Method
    受 Disscussion Method启发以及简化 My Method 代码，将判断条件挪到dfs里，代码更简洁清晰
    """
    if grid == []:
        return 0
    m = len(grid)
    n = len(grid[0])
    visit = [[0] * n for _ in range(m)]

    def dfs(i, j):
        if i < 0 or i > m - 1 or j < 0 or j > n - 1 or grid[i][j] == '0' or visit[i][j] == 1:
            return
        visit[i][j] = 1
        dfs(i, j + 1)
        dfs(i, j - 1)
        dfs(i + 1, j)
        dfs(i - 1, j)

    counter = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and visit[i][j] == 0:
                dfs(i, j)
                counter += 1
    return counter