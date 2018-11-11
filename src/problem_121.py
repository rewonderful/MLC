#!/usr/bin/env python
# _*_ coding:utf-8 _*_
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