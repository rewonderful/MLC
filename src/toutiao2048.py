import sys
import copy


def solution(key, matrix):
    if len(matrix) == 1:
        return matrix

    m, n = len(matrix), len(matrix[0])
    def find_next(i,j,i_delta,j_delta):
        while i < 4 and i >=0 and j >=0 and j < 4 and matrix[i][j] == 0 :
            i -= 1
        return i,j
    def clean_each(start_row,start_col,x_delta,y_delta):

        r = start_row
        for c in range(start_col):
            i = start_row
            base =
            while i < 4 and matrix[i][c] == 0:
                i += 1
            if i < 4:
                if matrix[i][c] == matrix[r][c]:
                    matrx[i][c] *= 2



        pass

    start_row  = 0
    start_col  = 0
    if key == 1:
        start = (m - 1, 0)
        direction = (-1, +1)
    elif key == 2:
        start = (0, 0)
        direction = (-1, +1)
    elif key == 3:
        start = (0, n - 1)
        direction = (+1, -1)
    else:
        start = (m - 1, 0)
        direction = (-1, +1)
    dp = copy.deepcopy(matrix)

    return dp

if __name__ == '__main__':

    key = int(input().strip())
    matrix = []
    for _ in range(4):
        matrix.append(list(map(int,input().strip().split(' '))))
    # for i in range()
    # matrix = [map(int,matrix[])]
    print(solution(key, matrix))