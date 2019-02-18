#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def combinationSum4(self, nums: 'List[int]', target: 'int') -> 'int':
    """
    算法：动规
    思路：
        我们需要一个一维数组dp，其中dp[i]表示目标数为i的解的个数，然后我们从1遍历到target，
    对于每一个数i，遍历nums数组，如果i>=x, dp[i] += dp[i - x]。这个也很好理解，比如说对于
    [1,2,3] 4，这个例子，当我们在计算dp[3]的时候，3可以拆分为1+x，而x即为dp[2]，3也可以拆
    分为2+x，此时x为dp[1]，3同样可以拆为3+x，此时x为dp[0]，我们把所有的情况加起来就是组成3
    的所有情况了
    """
    dp = [0 ]* (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    return dp[target]
def combinationSum4_(self, nums: 'List[int]', target: 'int') -> 'int':
    """

    TLE Method ,Brute Fore
    基本就是暴力求解
    do as they say
    从每一个num 开始进行探索，每次target - num向下传
    事实上这样作的时候，有很多重复计算，
    """
    self.ans = 0

    def dfs(target):
        if target < 0:
            return
        if target == 0:
            self.ans += 1
            return
        else:
            for num in nums:
                dfs(target - num)

    for num in nums:
        dfs(target - num)
    return self.ans
