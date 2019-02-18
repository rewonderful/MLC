#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def minDistance(self, word1: 'str', word2: 'str') -> 'int':
    """

    算法：动态规划dp
    思路：
        以前有一道题大概也是类似的，两个word互相转换，可以删除一个字母，添加一个字母或者替换一个字母，用dp做

        这个题只不过是只可以删除罢了。可以构建DP的关系来做
        可以吧word1和word2列成一个矩阵,矩阵的每个格子代表前i行字符串转换到前j列字符串最少需要经过几步
        加上空字符串是为了方便递推式的计算，显然答案就是dp[-1][-1]
        -----------------
       |   | ''  e  a  t |
       |-----------------|
       | ''| 0   1  2  3 |
       | s | 1   2  3  4 |
       | e | 2   1  2  3 |
       | a | 3   4  1  2 |
        -----------------
        初始条件，在边界处dp[i][j]就是当前下标i or j
        转换方程：
            如果word1[i] == word2[j]的话，那么当前字母就不需要考虑了，dp[i][j] = dp[i-1][j-1]
            否则：
                dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1]),即由左侧删除一个元素或者右侧删除一个元素，
            后再由上一级达到

        因为dp数组添加了空字符串''，所以在word1和Word2中索引字符的时候，要i-1 or j-1

        优化：
            由于目标解在最右下角，当前格子的值只取决于上一行和左侧这一列的值，所以可以用滚动数组的方式
            将2维空间缩减为1维
    """
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]