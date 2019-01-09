#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def exist(self, board, word):
    """
    My Method
    算法：回溯
    思路：
        比较典型的回溯题的思路，从某个位置出发看看某一处是否满足要求，在某个位置肯定是用BFS，对周围四个
    位置进行判断是否满足要求，如果满足要求的话就进一步bfs，每一次bfs判断一个字符，所以要有index来记录当前
    判断的是哪个字符，向下传入index+1，并且bfs的返回值应该是bool类型的，把bfs加入到if的判断条件中，
    在四周的四个方向进行探索，如果某个位置可行，就可以 return True了，如果四个位置都不可行，才 return False。
        注意要在探索的位置处用visited数组来记录探索的状态，避免造成循环，访问过的位置置True
        ❗️❗️❗️：
            并且如果某个位置不可行，要return False的时候，一定要把visited[i][j] = True置False，这样才可以保障
        回溯的时候，回溯到某一个位置visited还是原来的状态，因为如果某次探索对i，j置visited了并且这次探索的路径是错的，
        那么也会将i，j的visited置True导致回溯后下一次再从其他位置探索过来的时候由于此处i，j的visited已经是True了就不
        会再进行探索了。而i，j这个位置实际上是应该囊括在某一个解的路径中的。

        回溯一定要注意保存好回溯当前的状态！！！

        然后就是外面会有一个循环从所有符合word[0]的位置开始BFS
    """
    if word == '':
        return True
    if board == [] or board[0] == []:
        return False
    m = len(board)
    n = len(board[0])

    def bfs(x, y, index):
        i, j = x, y
        visited[x][y] = True
        if index == len(word) - 1:
            return True
        for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if x >= 0 and x <= m - 1 and y >= 0 and y <= n - 1 and not visited[x][y]:
                if board[x][y] == word[index + 1] and bfs(x, y, index + 1):
                    return True
        visited[i][j] = False
        return False

    visited = [[False] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):

            if board[i][j] == word[0] and bfs(i, j, 0):
                return True
    return False

def exist1(self, board, word):
    """

    Disscussion Method
    思路差不多，也是从4个方向进行探索，他这里虽然说是DFS，但是也和我理解的BFS差不多，都是从i,j位置的4个方向进行探索
    倒是这里用board本身而不借助visited数组，这个会省一点时间
    """
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian
    # check whether can find "word" along one direction
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res
if __name__ == '__main__':
    exist([["C","A","A"],["A","A","A"],["B","C","D"]],"AAB")