#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def calculateMinimumHP(self, dungeon):
    """
    My Method
    算法：动规
    思路：
        从右下角往左上角走，建立状态转移方程
        状态dp存的是在当前位置到达右下角Princess处最少需要多少血量
        注意dp的值总是>=1的，因为要求每一个位置的血量都不能<=0嘛，自然就要求血量>=1了

        先看边界条件，最右下角，如果dungeon[-1][-1]是正，那么血量为dp[-1][-1]=1，否则的话应该等于1-dungeon[-1][-1]
            如右下角dungeon值为5，那么血量为1就可以了，如果右下角为-5，那么至少需要6，dp[-1][-1]=6
        对最后一列和最后一行，因为只能朝右走或者朝下走，所以就考虑下一列或者下一行位置处的值
            如果dungeon[i][j] > dp[下一位置要求的最小血量]，隐含着dungeon[i][j]>0，那么dp[i][j]=1，
            否则需要补齐所需要的血量，下一位置要求Q，现在只有P，很显然Q-P即可
            其实就像建立边界条件时一样，边界条件建立时可以看做是dp[下一位置要求的最小血量]=1，所以如果>=1，就是1，
            否则的话就是1-dungeon[-1][-1]
        对于非最后一行和最后一列
            每个位置能朝右走或者向下走，那么很显然应该找min(right,down)值作下一位置要求的血量，然后计算思路同上
        最后返回dp[0][0]即可
    复杂度分析：
        时间：ON2，两层for循环
        空间：ON2，dp数组的大小
    """
    if dungeon == []:
        return 0
    m = len(dungeon)
    n = len(dungeon[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[-1][-1] = 1 if dungeon[-1][-1] > 0 else 1 - dungeon[-1][-1]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                continue
            elif i == m - 1:
                if dungeon[i][j] >= dp[i][j + 1]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j + 1] - dungeon[i][j]

            elif j == n - 1:
                if dungeon[i][j] >= dp[i + 1][j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j] - dungeon[i][j]
            else:
                min_dr = min(dp[i + 1][j], dp[i][j + 1])
                if dungeon[i][j] >= min_dr:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min_dr - dungeon[i][j]
    return dp[0][0]

def calculateMinimumHP1(self, dungeon):
    """
    My Method Plus
    与My Method一样，只不过简化了写法
    将if else 换成了 max 的写法
    解释：
        dp[下一位置要求的血量]肯定是 >= 1 的，
        dp[下一位置要求的血量] - dungeon[i][j]  大于0 说明当前房间血量不够，需要额外补充
        小于0 的话说明dungeon[i][j]>dp[下一位置要求的血量]，则令 dp[i][j] = 1
        用max(1,dp[下一位置要求的【最小】血量]-dungeon[i][j])就可以直接求出来dp[i][j]了
        与My Method一样，相比之下，简化了写法
    """

    if dungeon == []:
        return 0
    m = len(dungeon)
    n = len(dungeon[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[-1][-1] = 1 if dungeon[-1][-1] > 0 else 1 - dungeon[-1][-1]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                continue
            elif i == m - 1:
                dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j])
            elif j == n - 1:
                dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])
            else:
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
    return dp[0][0]