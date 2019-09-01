def coinChange( coins, amount):
    if amount == 0:
        return 0
    if len(coins) == 0:
        return -1
    coins.sort()
    if coins[-1] > amount:
        return -1
    dp = [-1] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        dp[coin] = 1
    for i in range(amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] != -1:
                if dp[i] == -1 or dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1

    return dp[-1]
if __name__ == '__main__':
    coinChange([1,231235],2)