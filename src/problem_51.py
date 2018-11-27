#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def solveNQueens0(self, n):
    """
    算法：递归/回溯/DFS
    思路：
            整体思路和My method 差不多，也是逐行去递归遍历搜索，但是该方法用一个一维列表去存储棋盘，更为高效
        这种解法用chessboard存储棋盘，其中下标i代表行，chessboard[i]代表列，即第row行col列的情况存储
        在col = chessboa[row]，这样可以节省大量的时间，并且不需要deepcopy辅助拷贝
            并且在判断是否可下棋的时候，只要判断当前这一行的chessboard[row]也就是col的值和已经存储起来的
        前面的每行的皇后摆放情况进行比较即可👉肯定已经不在那一行了，就判断是不是不属于之前第i行的col_i列以及
        对角线的位置即可
            最后返回结果时将一维数组chessboard 转为目标解的字符串二维数组形式即可
    复杂度分析：
        时间：不低，但My method强
        空间：不低，但My method强
    """

    def valid(chessboard, row):
        for i in range(row):
            if chessboard[i] == chessboard[row] or abs(chessboard[row] - chessboard[i]) == row - i:
                return False
        return True

    def dfs(chessboard, row, locations):
        if row == n:
            locations.append(chessboard[:])
            return
        for col in range(n):
            chessboard[row] = col  # 第row行放在第col列上
            if valid(chessboard, row):
                dfs(chessboard[:], row + 1, locations)

    locations = []
    ans = []
    dfs([-1] * n, 0, locations)

    for chess in locations:
        tmp = []
        for i in chess:
            tmp.append(''.join(['.' * i, 'Q', '.' * (n - i - 1)]))
        ans.append(tmp)

    return ans
def solveNQueens(n):
    import copy
    """
    My method
    算法：递归/回溯
    思路：
        n后问题是一个经典的回溯问题。我这里自己的方法复杂了一点，但是逻辑比较清晰
        首先一个基本的问题是，如何解这个问题？
            其实思路是比较明确的，尝试所有可能，然后将解添加到结果集中。按行逐行遍历，每行肯定只能放置
        一个皇后了，在row行col列尝试放置一个皇后，然后将其对应的位置放Q，row,col的行列，对角线位置都
        置为x不可放，这里注意对角线位置的判定就是行差和列差的绝对值是相等的就是对角线位置坐标ij的特征
        "剪枝"的话就是当前行有位置放才考虑去遍历下一行，否则不考虑
            我这里的做法将整个N后问题拆分成了比较明确的几个函数合作完成，其实主逻辑在generate这里，由
        putQueen更新棋盘，又因为题解的形式，要用list2str转换一下解的格式
        
        注意！
            1. 千万要注意Python浅拷贝深拷贝的坑，这里要频繁传递的是二维列表，对二维列表的拷贝，光用切片
        就不行了，chessboard[:]这种切片是浅拷贝，对列表中的引用也只是拷贝引用，为了在递归的过程中暂
        存每个递归处的棋盘状态，向下一层遍历传递的时候要传chessboard的深拷贝，用copy.deepcopy，将
        引用的每个元素内容也拷贝。这也导致用python做本题会更慢一些
            2. putQueen时，对行进行放置'x'的操作时注意range从row开始就好了，因为上面的row如果已经放置过
        皇后了，那么一定每一行除了Q就是x，况且我们是从上往下看的，我们只关心对后续行来说，我的每一列是什么状况，
        已经不需要考虑对前序行的棋盘面影响了。（当前放置的皇后一定不和前面的皇后冲突，所以就考虑对后续皇后的处理）
    复杂度分析：
        时间：高！事实上提交LeetCode时我的方法是有点压线过的，差点TLE超时
        空间：高！
    """
    def list2str(chessboard):
        str_chess = []
        for row in range(n):
            for col in range(n):
                if chessboard[row][col] == 'x':
                    chessboard[row][col] = '.'
            str_chess.append(''.join(chessboard[row]))
        return str_chess

    def putQueen(row,col,chessboard):
        chessboard[row][col] = 'Q'
        for i in range(row,n):
            for j in range(n):
                if (i == row or j == col or abs(i - row) == abs(j-col)) and chessboard[i][j] == '.':
                    chessboard[i][j] = 'x'
        return chessboard

    def generate(row,chessboard,result):
        if row > n-1:
            return
        for col in range(n):
            if chessboard[row][col] == '.':
                chess = putQueen(row,col,copy.deepcopy(chessboard))
                if row == n-1:
                    result.append(list2str(copy.deepcopy(chess)))
                generate(row+1,copy.deepcopy(chess),result)

    result = []
    chessboard = [['.' for i in range(n)] for j in range(n)]
    generate(0,chessboard,result)
    return result


if __name__ == '__main__':
    print(solveNQueens(4))