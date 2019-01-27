#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def maxCoins(self, nums):
    """
    HuaHuaJiang's Method
    算法：动规
    将序列分为 i...k....j
    用c[i][j]来表示从nums中第i到j能获取的最大收益，那么答案就是c[1][n]
    要将nums 填充，左侧填充1，右侧填充1，来达到nums[-1] = 1和nums[n+1] = 1

    第一层for的l代表的是序列长度，从短的序列开始考虑，从1开始，到n结束，l<=n 所以range末是 n+1
        第二层i代表开始的位置，自然是从1开始，到n-l+1结束，i <= n-l+ 1 所以range末是(n-l+1)+1
            序列长度是固定的，所以自然是j = i + l -1
            第三层k代表的是中间射击位置，所以k从i开始，到j结束，k <=j，所以range末是 j+1

    更多信息还是看写在博客中的图来了解吧
    """
    n = len(nums)
    nums = [1] + nums
    nums.append(1)

    c = [[0] * (n + 2) for _ in range(n + 2)]
    for l in range(1, n + 1):
        for i in range(1, (n - l + 1) + 1):
            j = i + l - 1
            for k in range(i, j + 1):
                c[i][j] = max(c[i][j], c[i][k - 1] + c[k + 1][j] + nums[k] * nums[i - 1] * nums[j + 1])
    return c[1][n]