#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def maxSubArray0( nums):
    """
    算法：动规
    思路：
        将动规状态dp(i)设置为以第i个元素结尾的子串的最大和，则：
        最优子结构：
            dp(i)与dp(i-1)的关系是，若dp(i-1)>0，则第i个元素结尾的子串最大和值为dp(i-1)+nums[i]
            否则的话就是nums[i]，毕竟小于0的数只会让当前和更小，不如不加
        重叠子问题：
            不是那么强烈
        边界条件：
            dp(0) = nums[0]

            具备以上条件后，就可以构造动规的解法了，求出以第i个元素结尾的子串的最大和
        注意：
            在记录过程中记得用max_res记录最大值！不是所有的动规都是返回dp[-1]，返回dp[-1]的是因为要求的问题的
        解就是动规状态的最后一个值，这里要求的是最大子串和！这里构造的递归状态，末尾的dp[-1]存储的是以nums[-1]，
        最后一个值作为子串的最大和是dp[-1],但是以nums[-1]为尾的子串和不一定是整个nums中最大的子串和！
    复杂度分析：
        时间：ON,遍历一次
        空间：ON，dp列表的空间
    """
    if not nums:
        return 0
    dp = [0] * len(nums)
    dp[0] = nums[0]
    max_res = dp[0]
    for i in range(1, len(dp)):
        #dp[i] = max(dp[i - 1] + nums[i], nums[i])
        dp[i] = dp[i - 1] + nums[i] if dp[i - 1] >= 0 else nums[i]
        max_res = max(max_res, dp[i])
    return max_res
def maxSubArray( nums):
    """
    算法："巧"解
    思路：
            遍历数组内的值，累加前面遍历过的元素的和，即当前子串的和，如果当前子串和sum是小于0的，是负数，那么就视
        这段子串和为0，因为，如果sum是负数，只会让和越来越小，所以就选择不用这段子串
    复杂度分析：
        时间：ON，遍历一遍
        空间：O1，常数级
    """
    #相当于是用当前值去加历史值，如果历史值小于0，负值，那么就应该抛弃历史序列，
    # 因为当前值（不论正负）加负值是一定比当前值更小的
    num_sum = 0
    max_sum = -float("inf")
    for num in nums:
        num_sum += num
        if num_sum > max_sum:
            max_sum = num_sum
        if num_sum < 0:
            num_sum = 0
    return max_sum
if __name__ == '__main__':
    nums = [1,-1,2,-2]
    maxSubArray(nums)