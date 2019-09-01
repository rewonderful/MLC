#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def rob(self, nums):
    """
    My Method
    循环起来的情况和普通的情况最关键的就是开头和结尾是不同的，因为形成了环使得开头和结尾成为了邻居
    对 1，2，3，4，5这样的序列来说，1抢了，5不能抢，5抢了，1不能抢
    而整条序列，可以看成两种情况，考不考虑第一个？
    如果考虑第一个，那么一定是在序列1，2，3，4中求最大收益，即5肯定不抢，放弃5
    如果不考虑第一个，那么一定是在序列2，3，4，5中求最大收益，即1肯定不抢，放弃1
    而一条序列对开头这个1来说，也就两种情况，抢或者不抢，因而可以从这里分割入手，将一个环变成两条序列
    将这两条序列的最大收益都求出来后，max一下就能得到环状态下的最大收益

    可优化部分：
        当前状态只取决于前序状态，所以可以用常数级空间来记录 pre 的值

    """
    if len(nums) == 0:
        return 0
    if len(nums) < 3:
        return max(nums)
    dp1 = [0] * (len(nums) - 1)
    dp1[0] = nums[0]
    dp1[1] = max(nums[0], nums[1])

    dp2 = [0] * (len(nums) - 1)
    dp2[0] = nums[1]
    dp2[1] = max(nums[1], nums[2])

    for i in range(2, len(dp1)):
        dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
        dp2[i] = max(dp2[i - 2] + nums[i + 1], dp2[i - 1])
    return max(dp1[-1], dp2[-1])