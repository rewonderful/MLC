#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def coinChange0( coins, amount):
    """
    算法：动规PLUS
    思路：
        其实和My OLD and TLE Method是一样的
        动规方程不变
        但是这里对边界值dp[0] = 0，做了很明确的规定，而且在后面的判断条件中，比我原生的naive思路更加合理
        即，不用排序coins，只要后面条件中加coin <= amount就行，并且不用遍历coins对dp[coin]赋值1，完全
        可以利用dp[coin] 与dp[0]的关系使dp[coin] = 1
            并且不用设置list，去求min，min(list)的时间复杂度是On，完全可以在for循环遍历coins的同时用if else
        就完成对dp[i]的更新，得到min(子状态)+1
    复杂度分析：
        时间：ONK,遍历一次amount长度的dp数组，遍历k个coin
        空间：ON，dp数组的空间
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
        以[1,2,5]，11为例，11所需要的最小钞票数就是11-1,11-2,11-5的子状态所需要的钞票数+1
        即dp(i) = min([dp(i-coin) for coin in coins])+1
        当前dp(i)由减去面额coin小于i的各子状态，用一张面额coin的钞票达到dp(i)

        边界条件dp(coin) =1 ,dp(0) = 0

        重叠子问题：
            算11的时候要算10，9，6，算10的时候要算9，8，4，也要算9，重叠子问题
        最优子结构：
            11所需要的最少的找零数就是10，9，6，数额最小找零数+1，其实也是状态转移方程

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

