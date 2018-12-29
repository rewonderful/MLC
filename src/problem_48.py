#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def rotate(matrix):
    """
    算法：旋转
    思路：
        按照题目的描述进行处理，
        注意到第i,j个位置的元素会转移到第j,n-i-1的位置去，暂且叫他为x,y，这个x也还会按照上述转移准则进行下一个位置的转移
        也就是说第ij个位置进行变换的时候，会顺时针的变换4个位置，并且这4个位置的坐标转换方式都是一样的，那么就可以腾笼换鸟，
        这个挪出去，下个补进来，如此一来就可以用O1的空间存储变换位置的值
            要注意i，j的下标，如果就粗暴地 in range(n) in range(n),那么挪腾了半天，乾坤大挪移后😂，各元素位置将保持不变
            注意，挪一个，就会动4个，一共是n2个元素，所以一共会挪n2/4次，两层for，差不多联想到各自n/2吧，（其实这样靠猜的
            想法挺不对的），首先可以很容易判断出来i是0到n//2，看j，首先j肯定不能到n-1-i，这样的话会替换i,0的旋转结果，也
            比较容易发现，然后就是j的其实位置，其实不难发现j的其实位置是i，对着草纸画一下就差不多清楚了，j是(i,n-i-1)
    复杂度分析：
        时间：ON2
        空间：O1
    """
    if matrix == [] or matrix[0] == []:
        return
    n = len(matrix)

    def get_rotate_xy(i, j):
        return (j, n - i - 1)

    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            x, y = get_rotate_xy(i, j)
            tmp = matrix[x][y]
            matrix[x][y] = matrix[i][j]
            while (x, y) != (i, j):
                x, y = get_rotate_xy(x, y)
                old = matrix[x][y]
                matrix[x][y] = tmp
                tmp = old


if __name__ == '__main__':
    matrix = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
    ],
    rotate(matrix)