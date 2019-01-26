#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""

"""


def nthUglyNumber(self, n):
    """
    Dissucussion Method
    第n个丑数一定是由更小的丑数通过*2，*3，*5得到的，即
    (A) 1×2, 2×2, 3×2, 4×2, 5×2, 6×2, 8×2…
    (B) 1×3, 2×3, 3×3, 4×3, 5×3, 6×3, 8×3…
    (C) 1×5, 2×5, 3×5, 4×5, 5×5, 6×5, 8×5…

    所以用3个因数分别为2，3，5的指针去指向三个序列A,B,C中当前所用到的丑数的位置，然后第k个丑数就是
    min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
    然后再将用到的那个序列的指针++ 后移
    """
    dp = [0] * n
    dp[0] = 1
    p2, p3, p5 = 0, 0, 0
    for i in range(1, n):
        dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
        if dp[p2] * 2 == dp[i]:
            p2 += 1
        if dp[p3] * 3 == dp[i]:
            p3 += 1
        if dp[p5] * 5 == dp[i]:
            p5 += 1
    return dp[-1]