#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def solution( board):
    """
    :type board: List[List[int]]
    :rtype: List[List[int]]
    """
    R,C = 5,5
    def dfs(i,j,curr):
        if i >= 0 and i < 5 and j >=0 and j<5 and board[i][j] == curr:
            board[i][j] = 0
            dfs(i,j+1,curr)
            dfs(i,j-1,curr)
            dfs(i+1,j,curr)
            dfs(i-1,j,curr)
            """
            for c in range(C):
            i = R - 1
            for r in reversed(range(R)):
                if board[r][c] > 0:
                    board[i][c] = board[r][c]
                    i -= 1
            for r in reversed(range(i + 1)):
                board[r][c] = 0
            
            """
    def clean(board):
        for col in range(C):
            for row in range(R-1,-1,-1):
                if board[row][col] == 0:
                    i = row - 1
                    while i > 0 and board[i][col] == 0:
                        i -= 1
                    if i >= 0:
                        board[row][col],board[i][col] = board[i][col],board[row][col]

    changed = True
    while changed:
        changed = False

        for i in range(R):
            for j in range(C - 2):
                if board[i][j] != 0 and board[i][j] == board[i][j + 1] == board[i][j + 2] and not changed:
                    dfs(i,j,board[i][j])
                    changed = True

        for i in range(R-2):
            for j in range(C):
                if board[i][j] != 0 and board[i][j] == board[i+1][j] == board[i+2][j] and not changed:
                    dfs(i, j, board[i][j])
                    changed = True

        clean(board)
    ans = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                ans += 1

    return ans
if __name__ == '__main__':
    # board = [[3 ,1, 2, 1, 1,],
    #          [1, 1, 1, 1, 3],
    #          [1 ,1 ,1 ,1, 1],
    #          [1, 1, 1, 1, 1],
    #          [3, 1, 2, 2, 2]]
    board = [[1, 1, 1, 1, 1, ],
             [1, 1, 1, 1, 1],
             [1, 1, 1, 1, 5],
             [1, 1, 5, 1, 1],
             [1, 1, 5, 5, 5]]
    # board = []
    # for _ in range(5):
    #     board.append(list(map(int,input().strip().split(" "))))

    print(solution(board))



