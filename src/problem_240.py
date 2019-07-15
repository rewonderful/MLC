#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix[0] == []:
            return False
        x, y = 0,len(matrix[0])-1
        while x < len(matrix) and y >= 0:
            if matrix[x][y] == target:
                return True
            elif target > matrix[x][y]:
                x += 1
            else:
                y -= 1
        return False
def searchMatrix(self, matrix, target):
    """
    算法：剥洋葱式解法
    思路：
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
            根据题目的描述，矩阵的特性是每一行升序，每一列升序，联想一维数组的二分查找，能应用
        二分查找是因为一维数组是有序的，target < nums[mid]就一定在左边，target > nums[mid]就一定
        在右边，而粗浅来看，中间的某个位置的话，如果target > matrix[i][j]，那么target的位置可能在
        i,j的右侧或者下方，甚至右上方也有可能，如果target < matrix[i][j]的话，那么target的位置可能
        在左侧或者上方，这样就不好固定某一个确切的方向了，但是！
            换个角度看，等于原来是两个方向，现在固定一个方向后再判断如果从右上角开始的话，右上角的数组，比如上面这个矩阵，
        如果大于15，target一定不在15所在的当前行！因为左侧的数字都小于15，所以一定转移到15的下一行去查找，因为当前行的数
        字都小于15，所以挪向下一行，这样一来就可以看做剥洋葱式的，将第一行剥离了，
            比如，在上面的矩阵中找12,首先从右上角开始，12小于15，一定不在15的那一列，剥掉，当前右上角元素
        就是11，12大于11，一定不在当前行，剥掉，转到下一行，现在右上角元素即matrix[i][j] == target == 12
        得到了结果
        [1,   4,  7, 11, 15],     [1,   4,  7, 11 ],
        [2,   5,  8, 12, 19],     [2,   5,  8, 12 ],    [2,   5,  8, 12 ],
        [3,   6,  9, 16, 22], --> [3,   6,  9, 16 ],--> [3,   6,  9, 16 ],
        [10, 13, 14, 17, 24],     [10, 13, 14, 17 ],    [10, 13, 14, 17 ],
        [18, 21, 23, 26, 30]      [18, 21, 23, 26 ]     [18, 21, 23, 26 ]
    ❗️❗️❗️：
        所以啊，一定要分析清问题的形式和特征，而且要灵活，不一定非要从左上角开始遍历，可以从右上角开始遍历！
    复杂度分析：
        时间：O(M+N)
        空间：O1
    """
    if matrix == [] or matrix[0] == []:
        return False
    i = 0
    j = len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return True
        elif target > matrix[i][j]:
            i += 1
        else:
            j -= 1
    return False


def searchMatrix1(self, matrix, target):
    """
    算法：遍历+二分
    思路：
        和74题的My Method 一模一样的方法，
        对可能包含答案的行依次二分搜索
        可能包含答案的行的特征是matrix[i][0] <= target <=matrix[i][-1]
        由于纵向每行是依次增大的，所以for i in range 扫描到某一行的行首元素
        matrix[i][0]都大于target了的话，那么这一行就不用看了， 直接break
        这种思路比较直观，但是并没有利用好题目数组的优势
    复杂度分析：
        时间：OklogN，k是matrix[i][0] < target的行数。N是matrix的列数，二分查找的时间
        空间：O1
    """
    if matrix == [] or matrix[0] == []:
        return False
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        if matrix[i][0] == target:
            return True
        elif matrix[i][0] < target:
            if matrix[i][-1] >= target:
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