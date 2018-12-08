#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def climbStairs(self, n):
    """
    算法：动态规划
    思路：
            爬楼梯的方式只有一次上1步或者一次上2步，所以第i个位置的状态state(i)只与state(i-1)，
        和state(i-2)有关，例如state(5)，第5个台阶不是从第3个台阶来的就是从第4个台阶来的。所以
        可以构造状态转移方程state(i) = state(i-1) + state(i-2)。这便是最优子结构，即当前解
        依赖于更小规模的解。并且画出来图后可以看到，第4个台阶不是从第3个来的就是从第2个来的，所以存在
        重叠子问题，将问题自底向上，解决了小问题后构筑大问题。
            程序的出口就是台阶数是1或者2的话就return n
    注意：
            动规构建问题的时候不一定要像01背包一样有二维表来记录一些值，可能只是一维数组就够了，即记录
        更小问题的结果，并且在更小问题的基础上构建更大问题的题解
    复杂度分析：
        时间：ON，遍历一遍
        空间：ON，steps数组的空间
    """
    if n == 1 or n == 2:
        return n
    steps = [0] * (n + 1)
    steps[1] = 1
    steps[2] = 2
    for i in range(3, n + 1):
        steps[i] = steps[i - 1] + steps[i - 2]
    return steps[-1]