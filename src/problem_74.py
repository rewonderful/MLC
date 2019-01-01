#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def searchMatrix0(self, matrix, target):
    """
    算法：二分查找
    思路：
        也是二分查找，不一样的是，根据题目的描述，可以将整个矩阵看成是一条龙排布的，也就是可以将
        整个矩阵看成是一个一维的数组，但是要搞明白这个二维矩阵和一维数组的下标对应关系，其实也很简单
        matrix[i][j] = matrixList[i*n+j]
        so
            i = index//n
            j = index%n
    """
    if matrix == [] or matrix[0] == []:
        return False
    m = len(matrix)
    n = len(matrix[0])
    lo = 0
    hi = m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        i = mid // n
        j = mid % n
        if matrix[i][j] == target:
            return True
        elif target < matrix[i][j]:
            hi = mid - 1
        else:
            lo = mid + 1
    return False
def searchMatrix(self, matrix, target):
    """
    My Method
    算法：二分查找
    思路：
        我的想法是要找的目标一定在哪个matrix[i][0] <= target的哪一行，所以先定位这一行然后再在这一行内
    进行二分查找
    """
    if matrix == [] or matrix[0] == []:
        return False
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        if matrix[i][0] == target:
            return True
        elif matrix[i][0] < target:
            lo = 0
            hi = n - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if matrix[i][mid] == target:
                    return True
                elif target < matrix[i][mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        else:
            break
    return False

