#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findTargetSumWays(self, nums, S):
    """
    HuaHuaJiang's Method
    算法：动规
    元素和是nums_sum，整个数组的元素取值范围就是[-nums_sum,+nums_sum]，所以总共可能有的状态值就是2*nums_sum+1
    因为列表下标都是正的，所以设定一个offset，
    如[1,1,1,1,1]，取值范围是[-5,-4,-3,-2,-1,0,1,2,3,4,5]，那么0那个位置的下标其实是5，所以offset=nums_sum
    dp[i][j]代表前i个元素构成j有几种方式
    dp第一维的大小是n+1，这样就可以把dp[0]用上，代表一个元素都不用的情况
    然后底下就是for循环了，如果dp[i][j] != 0的话，那么：
        如果加上nums[i]，那么下一行的dp[i+1][j+nums[i]] += dp[i][j]，就是多了从dp[i][j]来的次数
        如果减去nums[i]，那么下一行的dp[i+1][j-nums[i]] += dp[i][j]，就是多了从dp[i][j]来的次数
    这样便可以从上向下依次推出dp[i][j]的值
    最后返回的是dp[n][S+offset],要补上offset，因为数组下标实际上不是目标值，加上offset后才是

    然后可以看到dp[i]之和dp[i-1]有关系，所以第一维可以去掉，使用滚动数组，将二维dp数组化为一维dp数组
    """
    nums_sum = sum(nums)
    offset = nums_sum

    if nums_sum < S:
        return 0
    n = len(nums)
    dp = [[0] * (2 * nums_sum + 1) for _ in range(n + 1)]
    dp[0][offset] = 1

    for i in range(n):
        for j in range(2 * nums_sum + 1):
            if dp[i][j] != 0:
                dp[i + 1][j + nums[i]] += dp[i][j]
                dp[i + 1][j - nums[i]] += dp[i][j]

    return dp[n][S + offset]
def findTargetSumWays1(self, nums, S):
    """
    Brute Force Method
    Python TLE Java Accepted
    就递归，对每个元素进行加或者是减，看看最后到path末端的时候，和是S的话，ans += 1
    """
    self.ans = 0

    def dfs(index, path_sum):
        if index == len(nums):
            if path_sum == S:
                self.ans += 1
            return
        dfs(index + 1, path_sum + nums[index])
        dfs(index + 1, path_sum + -nums[index])

    dfs(0, 0)
    return self.ans
