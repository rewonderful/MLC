#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def maxProfit(self, prices):
    """
    :param self:
    :param prices:
    :return:
    股价数组中所有递增的片段，都是有收益的部分。加和就好了
    连着买卖就完事儿了，而且就算是价格是一直上升的状态，反正买卖无数次，当前卖了当天还可以再买，那不就是相当于
    当天没有做事情一样。所以直接每次的收益都加起来就好
    例如
    [4 7 8 2 8]
    最大利润很明显是 （8 - 4） + （8 - 2） = 10
    就因为这个式子让我想复杂了：首先要找到一个极小值4，然后找到极大值8；然后找到极小值2，然后找到极大值8；balabala……

    其实换一种思路，（7 - 4) + (8 - 7) + (8 - 2)
    区别在于，直接将后一个数减前一个数就好了呀，只不过如果后一个数比前一个数小的话就不考虑而已。
    """

    ans = 0
    if prices == []:
        return ans
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            ans += prices[i] - prices[i - 1]
    return ans