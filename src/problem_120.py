#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def minimumTotal0(self, triangle):
    """
    算法：动规/自底向上
    思路：
        要求第一行元素的最优选择路径，那么就应该选从底部上来到第二行中最优的，最小代价的那个元素
        dp(i,i) = min(dp(i+1,j),dp(i+1,j+1)) + triangle[i,i]
        自顶向下和自底向上的比较：
            自顶向下的时候，是下一层可达的所有位置考虑加上上一层中所有位置后当前行的最小值作为当前行的解
            要处理的会越来越多，而自底向下的话，一开始麻烦一点，后面要考虑的就会越来越少，所以自底向上更好

        自底向上的边界条件：
            dp[-1] = triangle[-1]
    复杂度分析：
        时间：ONK，N行，K为三角型最后那条边的长度
        空间：ONK，dp存储的空间
    """
    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle[-1]))]
    dp[-1] = triangle[-1]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
    return dp[0][0]
def minimumTotal1( triangle):
    """
    算法：动规/自顶向下
    思路：
        和上面自底向上的一样，显然自底向上的代码更简洁，自顶向下的话比较复杂繁琐一些
    """
    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle[-1]))]
    dp[0][0] = triangle[0][0]
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j > i-1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
    return min(dp[-1])

def minimumTotal( triangle):
    """
    ❌⚠️ My Wrong Method⚠️❌
    我这种解法实际上用的是贪心的思想！。即选择当前层最小的那个元素，下一层选择当前层最小的就好
    实际上不是的！
    如
        2
        -1  0
        -1  1 1
        50  50 -100
    如果按我这种方法的思路往下走的话，就会选择当前层最小的，而事实上要选择2,0,1,-100这条路径才是最小的！
    """
    dp = [(0, 0)] * len(triangle)
    dp[0] = (triangle[0][0], 0)

    for i in range(1, len(triangle)):
        last_index = dp[i - 1][1]
        last_value = dp[i - 1][0]
        curr_index = last_index
        curr_value = triangle[i][last_index]
        for neighbor in (-1, 1):
            j = neighbor + last_index
            if j >= 0 and j < len(triangle[i]) and triangle[i][j] < curr_value:
                curr_value = triangle[i][j]
                curr_index = j
        dp[i] = (curr_value+last_value, curr_index)
    return dp[-1][0]
if __name__ == '__main__':
    print(minimumTotal1([[2],[3,4],[6,5,7],[4,1,8,3]]))