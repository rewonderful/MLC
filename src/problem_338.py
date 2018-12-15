#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def countBits0(self, num):
    """
    Disscussion Method
    算法：动规
    思路：
        0: 0
        1: 1
        2: 10
        3: 11
        4: 100
        5: 101
        6: 110
        7: 111

        如果要找101有几个1，可以把末尾的1先去掉不看，就等于10中有几个1，再加上原来末尾的1的个数
        111中有几个1 --> 11中有几个1 再加上末尾的1的个数，末尾的1不是1个就是0个，因为末尾的1彰显了
        这个数是奇数还是偶数，向右侧chop off的时候直接i&1就好，如果末尾是1，则i&1的结果是1，否则是0
        所以
            dp[i] = dp[i>>1]+(i&1)
            i >> 1 basically means "chop off the last digit."
            i & 1 returns 0 if the last digit is 0, and 1 if it's 1.
    复杂度分析：
        时间：ON，遍历一次
        空间：ON，dp数组空间
    """
    dp = [0] * (num + 1)
    for i in range(1, num + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp
def countBits(self, num):
    """
    暴力解法
    将每个数字转换为二进制的字符串然后用count函数计算1的个数
    """
    result = []
    for i in range(num + 1):
        result.append(bin(i).count('1'))
    return result

def countBits1( num):
    """
    My DP Method
    算法：动规
    思路：
        我这里的递归是基于两个元素差值的方法，但是用了内置函数bin()，所以效率还是低一点
        找到距离i最近的2的幂次方
            如11最近的是8，那么dp[11] = dp[3]+1
            8最近的是8，do[8] = dp[0] + 1
        因为2的幂次方的dp值一定是1，所以根据二者的差值可以构造状态转移方程
    复杂度分析：
        时间：ONlogK，bin()需要logk，k为数字大小，N个数字，所以ONlogK
        空间：ON，dp数组大小
    """
    dp = [0] * (num + 1)
    for i in range(1, num + 1):
        last = 1 << (len(bin(i)[2:]) - 1)
        dp[i] = dp[i - last] + 1

    return dp
if __name__ == '__main__':
    print(countBits1(5))