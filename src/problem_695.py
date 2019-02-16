#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
    """

    算法：BFS
    思路：
        和DFS类似
        最主要的是要用return来返回某一个方向的计数值
    """
    self.ans = 0
    m = len(grid)
    n = len(grid[0])

    def bfs(i, j):
        area = 0
        if i >= 0 and i <= m - 1 and j >= 0 and j <= n - 1 and grid[i][j] == 1:
            area += 1
            grid[i][j] = 0
            area += bfs(i + 1, j) + bfs(i - 1, j) + bfs(i, j + 1) + bfs(i, j - 1)
        self.ans = max(self.ans, area)
        return area

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                bfs(i, j)
    return self.ans
def maxAreaOfIsland1(self, grid):
    """
    算法：DFS
    思路：
        对grid的每一处进行遍历，从1的位置开始DFS，计算每个方向上的1的个数，
        然后在dfs的过程中更新self.ans 为 最大的area值

        要注意将某个位置遍历后要将i，j的值设为0，gird[i][j] = 0 ，避免死循环
        用dfs，return 某一方向的计数值即可计算从某个1开始出发的四周的岛屿土地个数
    """
    self.ans = 0
    m = len(grid)
    n = len(grid[0])

    def dfs(i, j):
        area = 0
        if i >= 0 and i <= m - 1 and j >= 0 and j <= n - 1:

            if grid[i][j] == 1:
                area += 1
                grid[i][j] = 0
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    area += dfs(x, y)
        self.ans = max(self.ans, area)
        return area

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j)
    return self.ans

