#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def canPartition(self, nums):
    """
    Disscussion Method
    算法：动规

        首先如果数组的sum不是偶数的话，一定是不能分成两个子集的，return False
        否则的话，求出 target = sum(nums)//2
        原问题就转换为了：在数组nums中能不能挑选出部分元素使得其和为target

        所以可以构建动规方程，dp[i][j]表示前i个元素之和能否构成和为j

        这样问题就变成了一种特殊的01背包问题，
        当前元素i可以装或者不装，
        不装的话，dp[i][j] = dp[i-1][j]
        装的话，dp[i][j] = dp[i-1][j-nums[i]]

        注意，事实上构建dp的高和宽是len(nums)+1和target+1这样更好做一点，这样的话，dp[0][0] =True
        dp[0][j] = False,dp[i][0] = True
        这种加额外的一行or一列的操作相当于是padding
        但是要注意遍历的时候，dp数组中的i和nums中的i位置是相差1的。
    """
    num_sum = sum(nums)
    if num_sum % 2 != 0:
        return False
    target = num_sum // 2
    dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
    dp[0][0] = True
    for i in range(len(nums)):
        dp[i][0] = True
    for j in range(target):
        dp[0][j] = False
    for i in range(1, len(nums) + 1):
        for j in range(1, target + 1):
            dp[i][j] = dp[i - 1][j]
            if j - nums[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
    return dp[-1][-1]

def canPartition(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if nums == []:
        return True
    if sum(nums) % 2 == 1:
        return False
    target = sum(nums) / 2
    dp = [0] * (target + 1)
    dp[0] = 1
    for num in nums:
        i = target
        while (i >= num):
            dp[i] = dp[i] + dp[i - num]
            i = i - 1
    if dp[target] >= 2:
        return True
    else:
        return False
