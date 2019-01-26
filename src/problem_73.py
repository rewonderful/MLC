#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def setZeroes(self, matrix):
    """
    Sulotion Method
        将每一行的第一个元素和每一列的第一个元素作为flag位来记录该行or该列是否需要全部填为0，这样就避免了用额外的
    空间，相当于第一行or第一列作为了我的方法中用的集合。然后又由于是将行首和列首作为flag位，而遍历是依次向下的，
    所以不会存在将flag 0 和matrix中的0 混用的情况。然后左上角的matrix[0][0]既是行首也是列首，所以用了一个额外的
    is_col来记录col是不是0
    """
    is_col = False
    R = len(matrix)
    C = len(matrix[0])
    for i in range(R):
        if matrix[i][0] == 0:
            is_col = True
        for j in range(1, C):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, R):
        for j in range(1, C):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(C):
            matrix[0][j] = 0

    if is_col:
        for i in range(R):
            matrix[i][0] = 0
def setZeroes1(self, matrix):
    """
    My Brute Force Method
    用两个集合rows 和columns
    遍历一遍矩阵，记录下来所有0所在的行和列
    最后将所有行清空为0
    将所有列清空为0
    """
    if matrix == []:
        return
    rows = set()
    columns = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                columns.add(j)
    for row in rows:
        for j in range(len(matrix[0])):
            matrix[row][j] = 0
    for column in columns:
        for i in range(len(matrix)):
            matrix[i][column] = 0