#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def maxProfit0(self, prices):
    """
    这个是对下面思路的O1版本，因为当前状态只取决于上一个状态，所以可以用单个变量来记录关键的状态值
    """
    if prices == []:
        return 0

    holds_last = -prices[0]
    not_holds_last = 0
    not_holds_last2 = 0

    for i in range(1, len(prices)):
        holds = max(holds_last, not_holds_last2 - prices[i])
        not_holds = max(not_holds_last, holds_last + prices[i])

        holds_last = holds
        not_holds_last2 = not_holds_last
        not_holds_last = not_holds

    return max(holds_last, not_holds_last)
def maxProfit(self, prices):
    """
    Disscussion Method
    算法：动规+转换
    思路：
        和下面那个差不多，但是这个是更好理解的版本，首先要明确，股票有三个状态，买入，卖出，什么都不做
            那么某一天，一个人对股票的状态就是两种，持有股票holds，不持有股票not_holds，所以可以用holds和
        not_holds记录从开始到第i天的时候，第i天持有股票的最大收益，或者第i天不持有股票的最大收益，那么最后
        的ans 一定是二者之一即max(holds[-1],not_holds[-1])
            ok,看一下状态是怎么转换的
            如果第i天持有股票，那么要么就是从前一天转移过来的，也就是昨天。i-1就持有股票了，也就是这个股票
        不是第i天新买的，那么显然此时的最大收益是和holds[i-1]一样的，或者就是第i天的股票是新买的，要么是本来就有
        ，要么就是新买的，那么在买之前必须要卖出去手中的股票，而且因为有冷却期，所以必须在前天，i-2天卖出去股票，
        这样才可以在i-2天不持有股票，然后i-1天就是冷却期了，所以i-2天时不持有股票，这样才能在第i天买入
        股票，所以是not_holds[i-2]-prices[i]。
            事实上可以更细致地考虑，第i天买入股票的话，第i-1天一定是不持有股票的，否则第i天是不能买入的，那么
        第i-1天不持有股票的状态，来自于两个方面，一个是i-2天本来就不持有股票，二者是传承下来的，或者是第i-2天
        售出了股票，这样第i-1天本来就是冷却期，所以这时候真正起作用是i-2天本身的状态，对i-1来说，not_holds[i-2]
        的状态是已经确定的，那一天不持有股票的最大收益。其实看下面的递推式也可以理解，因为第i-1天一定是不能拥有
        股票的，而not_holds的状态来源于两个（1.保持，2.此天售出）,不可能是第二个，所以对第i天要新买入股票来说，
        必须是看第i-2天的not_holds状态。稍有点绕，或者就直观地，第i天想买，一定是第i-2天不持有股票后第i天才买
            holds[i] = max(holds[i - 1], not_holds[i - 2] - prices[i])
            如果第i天是不持有股票的，那么要么就是和前一天一样啥也没做转移过来的，即not_holds[i-1],要么就是
        前一天是持有股票的，今天再卖出，那么就是holds[i-1]+prices[i]
            not_holds[i] = max(not_holds[i - 1], holds[i - 1] + prices[i])

        holds[0] = -prices[0] 可以理解为，第一天本来就口袋空空，那么还想买股票持有，
        那么就要花prices[0]的价格去买，此时持有股票的收益就是-prices[0]
    """
    if prices == []:
        return 0
    if len(prices) == 1:
        return 0
    if len(prices) == 2:
        sub = prices[1] - prices[0]
        return max(sub, 0)
    holds = [0] * len(prices)
    not_holds = [0] * len(prices)
    holds[0] = -prices[0]
    not_holds[0], not_holds[1] = 0, 0

    for i in range(1, len(prices)):
        holds[i] = max(holds[i - 1], not_holds[i - 2] - prices[i])
        not_holds[i] = max(not_holds[i - 1], holds[i - 1] + prices[i])
    return max(holds[-1], not_holds[-1])
def maxProfit1(self, prices):
    """
    Disscussion Method
    算法：状态转换
    思路：
        某时刻的股票只有三种状态，买入，卖出，或者什么都不做
            根据Disscussion中原作者画的图，某一时刻的情况可以画成三个状态节点s0,s1,s2,这三个状态不是直接想到的就有
        三个状态，而是通过状态转换的可能性得出来的共有三种状态，并且是对第ith的股票的状态描述。
            并且看图可以发现，每一时刻的状态只取决与上一个时刻的状态，就像N皇后可以将二维数组变成一维数组一样，所以
        可以将空间复杂度降低到O1
            这三个状态其实相当于是
            s0:can buy  初始为0，
            s1:can sell 初始为-prices[0]，因为要卖只能卖第一个
            s2:take a rest 初始为0
        最后的最大收益一定是来自于s2或者s0，因为s1是买股票后。肯定不是最大的

    复杂度：
        时间：ON
        空间：O1
    """
    if prices == []:
        return 0
    s0 = 0
    s1 = -prices[0]
    s2 = 0
    for i in range(len(prices)):
        pre0 = s0
        pre1 = s1
        pre2 = s2
        s0 = max(pre0, pre2)
        s1 = max(pre1, pre0 - prices[i])
        s2 = pre1 + prices[i]
    return max(s2, s0)