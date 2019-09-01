#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def maxProfit7( prices) :
    """

    :param prices:
    :return:
    用 buy 来记录遍历到当前时刻的最小buy
    用 sell - buy 来记录截止到目前，以当前sell出售时的gain
    """
    gain = 0
    if prices == []:
        return gain
    buy = prices[0]
    for sell in prices:
        buy = min(buy, sell)
        gain = max(gain, sell - buy)
    return gain
def maxProfit( prices):
    """
    :type prices: List[int]
    :rtype: int

    """
    if len(prices) < 2:
        return 0
    profit = 0
    minimum = prices[0]
    for i in prices:
        minimum = min(i, minimum)
        profit = max(i - minimum, profit)
    return profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))