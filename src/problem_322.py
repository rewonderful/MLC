#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def coinChange0( coins, amount):
    """
    算法：
    思路：
    复杂度分析：
        时间：
        空间：
    """
    dp = [-1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= amount and i - coin >= 0 and dp[i - coin] != -1:
                if dp[i] == -1 or dp[i] > dp[i - coin] + 1:
                    dp[i] = dp[i - coin] + 1
    return dp[-1]
def coinChange( coins, amount):
    """
    ❌⚠️My OLD and TLE Method
    算法：动态规划
    思路：
        以组成当面面额所需要的最少的钞票数量为状态，

    复杂度分析：
        时间：大！
        空间：大
    """

    if amount == 0:
        return 0
    coins.sort()
    min_coin = coins[0]
    if min_coin > amount:
        return -1

    for i in range(len(coins) - 1, -1, -1):
        if coins[i] <= amount:
            coins = coins[:i + 1]
            break
    dp = [-1] * (amount + 1)
    for i in range(1, amount + 1):
        if  i in coins:
            dp[i] = 1
            continue
        sub = []
        for coin in coins:
            if coin <= amount and i - coin >= 0 and dp[i - coin] != -1:
                sub.append(dp[i - coin])
        if sub != []:
            dp[i] = min(sub) + 1
    return dp[-1]
if __name__ == '__main__':
    import time
    start = time.time()
    print(coinChange([125,146,125,252,226,25,24,308,50,9999],8402))
    end = time.time()
    print(float(end-start))