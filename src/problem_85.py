#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def maximalRectangle( matrix):
    """
    Disscussion Method
    算法：单调栈
    思路：
        本题的思路是将原问题转化为类似于84题的形式然后求解。非常巧妙！
            关键一步就是将问题转化，可以将矩形分解为长乘宽，或者说底乘高，那么可以遍历矩阵的行，以每一行的1的位置做底，
        这一行上第i个位置这一列中'1'的个数做高，就可以构建出一个直方图，便在当前这一行中构建出了第84题的形式，用
        单调栈求解即可。那么对整个matrix的所有row遍历构建直方图计算矩形面积，就可以求解出整个矩形中的最大'1'矩形面积。

        要理解👆这种分解一行一行，自上向下累计直方图的方式，是一定能遍历完所有矩阵中的矩形的。

        假设把矩阵沿着某一行分开，然后把分开的行作为底面，将自底面往上的矩阵看成一个直方图（histogram）。
     直方图的中每个项的高度就是从底面行开始往上1的数量。根据Largest Rectangle in Histogram就可以求出
     当前行作为矩阵下边缘的一个最大矩阵。接下来如果对每一行都做一次Largest Rectangle in Histogram，
     从其中选出最大的矩阵，那么它就是整个矩阵中面积最大的子矩阵。

        如何计算某一行为底面时直方图的高度呢？如果重新计算，那么每次需要的计算数量就是当前行数乘以列数。
     然而会发现一些动态规划的踪迹，如果知道上一行直方图的高度，就只需要看新加进来的行（底面）上对应的列
     元素是不是0，如果是，则高度是0，否则则是上一行直方图的高度加1。利用历史信息，就可以在线行时间内
     完成对高度的更新。由于Largest Rectangle in Histogram的算法复杂度是O(n)。所以完成对一行为底边的
     矩阵求解复杂度是O(n+n)=O(n)。接下来对每一行都做一次，那么算法总时间复杂度是O(m*n)。

    """
    if matrix == [] or matrix[0] == []:
        return 0
    ans = 0
    height = [0] * (len(matrix[0]) + 1)

    for row in matrix:
        for i in range(len(row)):
            height[i] = height[i] + 1 if row[i] == '1' else 0
        stack = [-1]
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                index = stack.pop()
                h = height[index]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
    return ans
if __name__ == '__main__':
    print(maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))