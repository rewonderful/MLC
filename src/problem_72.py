#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def minDistance7( word1, word2):
    """
    :param word1:
    :param word2:
    :return:

     注意当word1[i - 1] != word2[j - 1]的话，⬅️↖️⬆️三种都要考虑，相当于insert,replace,delete
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0
    for j in range(1, n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        dp[i][0] = i
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[-1][-1]
def minDistance(self, word1, word2):
    """
    Solution Method With Mine
    算法：动规
    思路：
        首先看题目意思就能很容易地想到用动规，因为是求最小嘛
            下面代码的动规状态建立的是dp[i][j]，代表的是word1的第i个位置以前与word2第j个位置以前要建立
        转换最少需要多少步，显然dp[-1][-1]就是要求的目标，可以画一个表看出来，
            dp[i][j] 的值取决于左侧，上面，左上三个位置，分别对应于：
            以horse 和 ros 为例
                左：dp[i][j-1]      --> horse 到 ro 的距离，那么从左侧过来就代表insert ros的s
                上：dp[i-1][j]      --> horse 到 ros 的距离，从上面过来就代表delete horse的e
                左上：dp[i-1][j-1]  --> hors 到 ro  的距离，从左上过来就代表replace horse的e为s
            这里要注意左上是特殊的如果现在词是horss，那么horss到ros的距离和hors到ros的距离是一样的，
            因为末尾的字母都一样，所以不需要+1
            if word1[i] == word2[j]:
                dp[i][j] = 1+ min(left,top,left_top-1)
            else:
                dp[i][j] = 1+ min(left,top,left_top)
            显然边界条件在dp[0][0],dp[0][j],dp[i][0]
            画个表也可以比较清晰的找到他们的关系和值
            要注意的是在边界位置也要考虑word1[i]和word2[j]的关系！比如horse到r的距离，
            显然在hor的时候，因为hor的末尾是r，所以hor的距离和ho是一样的，第一行h到ros的距离计算的时候同理
    """

    n = len(word1)
    m = len(word2)
    if n * m == 0:
        return n + m
    dp = [[float('inf')] * m for _ in range(n)]
    dp[0][0] = 0 if word1[0] == word2[0] else 1
    for j in range(1, m):
        if word1[0] == word2[j]:
            dp[0][j] = dp[0][j - 1]
        else:
            dp[0][j] = dp[0][j - 1] + 1
    for i in range(1, n):
        if word1[i] == word2[0]:
            dp[i][0] = i
        else:
            dp[i][0] = dp[i - 1][0] + 1
    for i in range(1, n):
        for j in range(1, m):
            if word1[i] != word2[j]:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j])
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j - 1] - 1, dp[i - 1][j])
    return dp[-1][-1]

def minDistance1(self, word1, word2):
    """
    Solution Method
     算法：动规
     思路：
        整体思路和上面的一样，不同的是这里dp状态的下标含义有所不同
        定义dp[n+1][m+1]
        dp[i][j]代表word1从第1个字母到第i个字母与word2第1个字母到第j个字母之间转化时的最小距离
        所以dp[0][0]这类代表空字符串到word2的转化，比如''到'ros'，那么这一行dp[0][j]的值自然就是j了
        即全靠insert
        dp的状态转移方程不变。

        这种定义dp的解法更简洁
    """

    n = len(word1)
    m = len(word2)
    if n * m == 0:
        return n + m
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] != word2[j - 1]:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j])
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j - 1] - 1, dp[i - 1][j])
    return dp[-1][-1]