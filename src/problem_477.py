#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def totalHammingDistance( nums):
    """
    HuaHuaJiang's Method
    看数据规模，数组长度是"Length of the array will not exceed 10^4."，所以不能用ON2

    看下面这个例子，4，14，2和1：
    4:     0 1 0 0

    14:    1 1 1 0

    2:     0 0 1 0

    1:     0 0 0 1
    其实要求的海明距离就是每一列的海明距离之和
    那么每一列的海明距离，其实就是1的个数乘0的个数，所以可以统计出每一列1的个数，而这些数字又不会超过10^9
    也就是不会超过2^32次
    那么就可以循环32次，对每一列求1的个数，设置一个mask=1，和num做与操作即可取出某一位是否为1，如果相与后
    不为0，那么就说明num的这一位为1，counter += 1，
    for 遍历完所有数字后， ans += (len(nums) - counter) * counter

    最后mask左移一位 mask <<= 1,对下一位（下一列）计算1的个数


    "我们先看最后一列，有三个0和一个1，那么它们之间相互的汉明距离就是3，即1和其他三个0分别的距离累加，
    然后在看第三列，累加汉明距离为4，因为每个1都会跟两个0产生两个汉明距离，同理第二列也是4，第一列是3。
    我们仔细观察累计汉明距离和0跟1的个数，我们可以发现其实就是0的个数乘以1的个数，发现了这个重要的规律，
    那么整道题就迎刃而解了，只要统计出每一位的1的个数即可"
    """
    ans = 0
    mask = 1
    for i in range(32):
        counter = 0
        for num in nums:
            if num & mask:
                counter += 1
        ans += (len(nums) - counter) * counter
        mask <<= 1
    return ans
if __name__ == '__main__':
    print(totalHammingDistance([4, 14, 2]))