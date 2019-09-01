#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def maxProfit(prices) :
    """
    :param prices:
    :return:
    两次买卖，而且必须要分开，所以可以把整个数组化为两个区间，[0:i],[i:-1]，记为left，right
    那么两次交易的gain也就是left_gain+right_gian,
    要注意的是两次交易的关系不是贪心的，左边最大，得到最大的卖出点i后，右边可能right_gain太小。
    所以要运用dp的思想，相当于是2次遍历。
    对每个位置i，有两种方式
        1. 从左往右，前面时刻买入，截止到i之前发生交易的最大收益left_gain
        2. 从右往左，后面时刻以最高值卖出，截止到i时刻发生交易的最大收益right_gain
    那么答案就相当于是max([left_gain[i]+right_gian[i])
    所以解题方法就是分别左右两次遍历。得到买卖收入，然后再第二次遍历的时候，就已经可以直接用
    ans = max(ans,left[i]+right[i])来得到了
    """
    if prices == []:
        return 0
    left_dp = [0] * len(prices)
    left_min = prices[0]
    left_gain = 0
    for i in range(1, len(prices)):
        left_min = min(left_min, prices[i])
        left_gain = max(left_gain, prices[i] - left_min)
        left_dp[i] = left_gain
    right_dp = [0] * len(prices)
    right_max = prices[-1]
    right_gian = 0
    ans = 0
    for i in range(len(prices) - 1, -1, -1):
        right_max = max(right_max, prices[i])
        right_gian = max(right_gian, right_max - prices[i])
        right_dp[i] = right_gian
        ans = max(ans, right_dp[i] + left_dp[i])
    return ans
if __name__ == '__main__':
    print(maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))