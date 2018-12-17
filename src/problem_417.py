#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def pacificAtlantic( matrix):
    """
    Disscussion Method
    算法：BFS
    思路：
        关键是要拆成两个方向去找！分别找到后求交集！
        直接求得同时能到达两个海洋的条件不好做！
        曲线救国，曲线思维
        ------------------------------------------------------------------------------------------------
            首先还是考虑暴力解法的思维，即对每个点，都DFS看看能不能从这个点出发到达另外一侧，如果可以的话就add到ans中
            这就意味着会套好多好多for循环，对每个i,j都DFS一遍显然是非常耗时的！并且可以推敲出来，本题不能用动规DP做！

            将本题拆为两个方向来看，即对两个海洋先分别判断哪些位置可以抵达，将双方可以抵达的位置集合求交集不就是问题的答案吗！
            而求抵达某一个海洋的求解思路又比较明确！就像542题一样，542中我不从1出发，从0出发，这里我从已知可达海洋的位置出发，
        用BFS看周围的r,c位置，如果符合条件，就可以一次性将多个r,c位置更新为可达状态，而不是暴力的思想中一次只关注一个位置！
        将符合条件的rc添加到set中来，要注意这里要去重，如果rc已经在set中就不要添加了，并且不要入队列，否则已经扩展开的rc再
        扩展会回去，等于进入了有环图！⚠️⚠️⚠️💥🌟⚡️🌟
    复杂度分析：
        时间：ON2？不太会算
        空间：ON2，ans空间
    """
    ans = []
    if not matrix or not matrix[0]:
        return ans
    m = len(matrix)
    n = len(matrix[0])
    pacific_reachble = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
    pacific_reachble = set(pacific_reachble)
    atlantic_reachble = [(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m)]
    atlantic_reachble = set(atlantic_reachble)

    def bfs(ocean_reachble):
        queue = list(ocean_reachble)
        while queue:
            i, j = queue.pop(0)
            for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if r >= 0 and r <= len(matrix) - 1 and c >= 0 and c <= len(matrix[0]) - 1:
                    if matrix[r][c] >= matrix[i][j] and (r, c) not in ocean_reachble:
                        queue.append((r, c))
                        ocean_reachble.add((r, c))
        return ocean_reachble

    return list(bfs(pacific_reachble) & bfs(atlantic_reachble))




def pacificAtlantic1( matrix):
    """
    My Ridiculous Method
    原来的思路：
        我原来的想法是首先看到了左下角和右上角是一定可达的，然后想到了这是"边界条件"，每个i,j位置设置[BOOL,BOOL]两个状态值
    表征当前点能不能到达[Pacific,Atlantic]，利用542题的思路，上下左右四个方向，2个方位一起的遍历，↙️一次↗️一次。并且每个位
    置的[Pacific,Atlantic,]值是比较容易计算的，矩形的四周都是特殊状态然后想用DP来着，后来发现DP会缺少遍历的情况，对本题的初
    始示例来说，如果用"DP"，那么1,4将永远无法添加到ans中，因为dp总是从一层往外扩的，其基于的是状态转移方程，而我一次性要判断出
    两个BOOL状态，用dp无法同步两个状态，除非我用两次方位，每次都只判断能否到达一个海洋，这样的话其实就是上面的BFS方法！
        下面的代码就比较迷了，想用队列的形式进行BFS，并且直接判断某个位置r,c能否到达两个海洋，即题解
    """
    ans = []
    if matrix == []:
        return []
    reachble = [[[j == 0, i == len(matrix) - 1] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    # [Pacific,Atlantic,]
    # 从右上角开始BFS
    queue = [(len(matrix)-1, 0)]
    while queue:
        i, j = queue.pop(0)
        if reachble[i][j][0] and reachble[i][j][1]:
            ans.append([i, j])
        for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if r >= 0 and r <= len(matrix) - 1 and c >= 0 and c <= len(matrix[0]) - 1:
                if not reachble[r][c][0]:
                    if matrix[r][c] >= matrix[i][j]:
                        reachble[r][c][0] = reachble[i][j][0]
                if not reachble[r][c][1]:
                    if matrix[r][c] >= matrix[i][j]:
                        reachble[r][c][1] = reachble[i][j][1]
                if (reachble[r][c][0] or reachble[r][c][1]) and (r,c) not in reachble:
                    queue.append((r, c))
    return ans
if __name__ == '__main__':
    print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))